import logging
import unittest

debug = logging.getLogger(__name__).debug


def input_ints():
    return list(map(int, input().strip().split()))


def _main():
    n, k = input_ints()
    if k == 1:
        print(0)
    else:
        print(n - k)


class Test(unittest.TestCase):
    def setUp(self):
        import run
        self._test = run

    def test_main(self):
        self._test.test_files(self, _main)


if __name__ == '__main__':
    _main()
