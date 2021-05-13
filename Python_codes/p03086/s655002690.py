#
# abc122 b
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
        input = """ATCODER"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """HATAGAYA"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """SHINJUKU"""
        output = """0"""
        self.assertIO(input, output)


def resolve():
    S = input()

    ans = 0
#    for i in range(len(S)):
#        t = 0
#        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
#            t += 1
#            for j in range(i+1, len(S)):
#                if S[j] == "A" or S[j] == "C" or S[j] == "G" or S[j] == "T":
#                    t += 1
#                else:
#                    break
#        ans = max(ans, t)

    ans = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            if S[i:j].count("A") + S[i:j].count("C") + S[i:j].count("G") + S[i:j].count("T") == len(S[i:j]):
                ans = max(ans, len(S[i:j]))
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
