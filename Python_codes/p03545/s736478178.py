#
# abc079 c
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
        input = """1222"""
        output = """1+2+2+2=7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0290"""
        output = """0-2+9+0=7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3242"""
        output = """3+2+4-2=7"""
        self.assertIO(input, output)


def resolve():
    N = input()

    for bit in range(1 << 3):
        S = ""
        for j in range(3):
            S += N[j]
            if bit & (1 << j) == 0:
                op = "+"
            else:
                op = "-"
            S += op
        S += N[3]
        if eval(S) == 7:
            print(S+"=7")
            break


if __name__ == "__main__":
    # unittest.main()
    resolve()
