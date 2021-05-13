import sys
from io import StringIO
import unittest
import os
import math

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


# 実装を行う関数
def resolve(test_def_name=""):
    a, b, c, d = map(int, input().split())

    ans = b - a + 1

    all_cnt = -(b // c + b // d) + b // (lcm(c, d))
    out_cnt = -((a - 1) // c + (a - 1) // d) + (a - 1) // (lcm(c, d))

    print(ans + all_cnt - out_cnt)


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
        test_input = """4 9 2 3"""
        output = """2"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """10 40 6 8"""
        output = """23"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """314159265358979323 846264338327950288 419716939 937510582"""
        output = """532105071133627368"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def tes_t_1original_1(self):
        test_input = """データ"""
        output = """データ"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
