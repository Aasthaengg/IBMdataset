import unittest


def solve(n, a):
    # 貪欲
    cnt = 0
    total = a[0]
    if a[0] < 1:
        cnt = abs(a[0]) + 1
        total = 1
    for i in range(1, n):
        if i % 2 == 0:  # +
            if total + a[i] > 0:
                total += a[i]
            else:
                diff = abs(total + a[i]) + 1
                cnt += abs(diff)
                total = 1
        else:  # -
            if total + a[i] < 0:
                total += a[i]
            else:
                diff = abs(total + a[i]) + 1
                cnt += abs(diff)
                total = -1
    t = cnt
    cnt = 0
    total = a[0]
    if a[0] > -1:
        cnt = abs(a[0]) + 1
        total = -1
    for i in range(1, n):
        if i % 2 == 0:  # -
            if total + a[i] < 0:
                total += a[i]
            else:
                diff = abs(total + a[i]) + 1
                cnt += abs(diff)
                total = -1
        else:  # +
            if total + a[i] > 0:
                total += a[i]
            else:
                diff = abs(total + a[i]) + 1
                cnt += abs(diff)
                total = 1

    return min(t, cnt)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = solve(n, a)
    print(result)


if __name__ == "__main__":
    main()


class Test(unittest.TestCase):
    def test_solve_1(self):
        n = 4
        a = [1, -3, 1, 0]
        actual = solve(n, a)
        expected = 4
        self.assertEqual(actual, expected)

    def test_solve_2(self):
        n = 5
        a = [3, -6, 4, -5, 7]
        actual = solve(n, a)
        expected = 0
        self.assertEqual(actual, expected)

    def test_solve_3(self):
        n = 6
        a = [-1, 4, 3, 2, - 5, 4]
        actual = solve(n, a)
        expected = 8
        self.assertEqual(actual, expected)

    def test_solve_4(self):
        n = 6
        a = [-1, 2, -2, 2, -2, 1000]
        actual = solve(n, a)
        expected = 0
        self.assertEqual(actual, expected)
