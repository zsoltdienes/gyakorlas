from unittest.mock import patch

from randomizer import get_random_number


def test_returns_int():
    assert isinstance(get_random_number(), int)


def test_within_range():
    for _ in range(1000):
        value = get_random_number()
        assert 1 <= value <= 100


def test_can_return_lower_bound():
    with patch("random.randint", return_value=1):
        assert get_random_number() == 1


def test_can_return_upper_bound():
    with patch("random.randint", return_value=100):
        assert get_random_number() == 100


def test_calls_randint_with_correct_args():
    with patch("random.randint", return_value=42) as mock_randint:
        result = get_random_number()
    mock_randint.assert_called_once_with(1, 100)
    assert result == 42
