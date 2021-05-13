import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    s = list(input())

    s.reverse()

    devval = pow(10, 9) + 7

    dp = [[0 for i in range(13)] for i in range(100001)]

    # 初期値設定
    if s[0] == "?":
        for j in range(10):
            dp[0][j] += 1
    else:
        dp[0][int(s[0]) % 13] += 1

    # DP
    for i in range(1, len(s)):
        for j in range(10):
            if s[i] != "?" and s[i] != str(j):
                continue

            # ここを改善しないと無理。pow(10,100万)とか不可能・・。TLE・・。
            aaa = j * pow(10, i, 13)

            # 前DPの値を今DPに加算
            for k in range(13):
                dp[i][(aaa + k) % 13] = (dp[i][(aaa + k) % 13] + dp[i - 1][k] % devval) % devval

    # 余り5の要素数が答え
    print(dp[len(s) - 1][5])


# テストクラス
class TestClass(unittest.TestCase):
    def assertIO(self, assert_input, output):
        stdout, sat_in = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(assert_input)
        resolve(sys._getframe().f_back.f_code.co_name)
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, sat_in
        self.assertEqual(out, output)

    def test_input_1(self):
        test_input = """??2??5"""
        output = """768"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """?44"""
        output = """1"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """7?4"""
        output = """0"""
        self.assertIO(test_input, output)

    def test_input_4(self):
        test_input = """?6?42???8??2??06243????9??3???7258??5??7???????774????4?1??17???9?5?70???76???"""
        output = """153716888"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def test_1original_1(self):
        test_input = """?"""
        output = """1"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
