import sys
from io import StringIO
import unittest


def resolve():
    l, r = map(int, input().split())
    ll = []

    for i in range(l, r + 1, 1):
        if i % 2019 in ll:
            break
        else:
            ll.append(i % 2019)

    ll.sort()
    ans = 2020

    for i in range(len(ll)):
        for j in range(i + 1, len(ll)):
            tmp = (ll[i] * ll[j]) % 2019
            if tmp < ans:
                ans = tmp

    print(ans)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """2020 2040"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5"""
        output = """20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
