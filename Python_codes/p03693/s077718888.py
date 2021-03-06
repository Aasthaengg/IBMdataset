#
# abc064 a
#
import sys
from io import StringIO
import unittest


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
        input = """4 3 2"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 4"""
        output = """NO"""
        self.assertIO(input, output)


def resolve():
    r, g, b = map(int, input().split())
    x = 100*r + 10*g + b
    ans = "NO"
    if x % 4 == 0:
        ans = "YES"
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
