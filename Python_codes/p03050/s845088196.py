import unittest


def solve_small(n):
    total = 0
    for m in range(1, n):
        if n // m == n % m:
            total += m
    return total


def solve(n):
    if n == 1:
        return 0
    conds = set()
    conds.add(n-1)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            conds.add(i-1)
            conds.add(n // i - 1)
    total = 0
    for m in list(conds):
        if n // m == n % m:
            total += m
    return total


def main():
    n = int(input())
    result = solve(n)
    print(result)


if __name__ == "__main__":
    main()


class Test(unittest.TestCase):
    def test_solve_1(self):
        n = 8
        actual = solve(n)
        expected = 10
        self.assertEqual(actual, expected)

    def test_solve_2(self):
        n = 1000000000000
        actual = solve(n)
        expected = 2499686339916
        self.assertEqual(actual, expected)
