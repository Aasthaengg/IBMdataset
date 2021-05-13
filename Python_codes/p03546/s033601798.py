from types import CodeType
import unittest


def solve():
    return 0


def main():
    h, w = map(int, input().split())
    c = [list(map(int, input().split())) for i in range(10)]
    a = [list(map(int, input().split())) for i in range(h)]

    for k in range(10):
        for i in range(10):
            for j in range(10):
                if c[i][k] + c[k][j] < c[i][j]:
                    c[i][j] = c[i][k] + c[k][j]
    total = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == -1:
                continue
            total += c[a[i][j]][1]
    print(total)


if __name__ == "__main__":
    main()


class Test(unittest.TestCase):
    def test_case1(self):
        expected = 0
        actual = solve()
        self.assertEqual(actual, expected)
