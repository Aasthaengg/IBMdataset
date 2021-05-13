import math
import os
import sys
import unittest
from io import StringIO

# 検索用タグ、3次元->2次元で解く。次元を落とす。、直角三角形、2辺の長さから角度を求める(アークタンジェント、atan())
# 参考：https://drken1215.hatenablog.com/entry/2020/04/26/193500

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve():
    # 数値取得サンプル
    #   1行N項目 x, y = map(int, input().split())
    #   N行N項目 x = [list(map(int, input().split())) for i in range(n)]

    # 文字取得サンプル
    #   1行1項目 x = input()
    a, b, x = map(int, input().split())
    x = x / a

    # 45度以上傾けるかどうか(xが全体の半分以下なら、45度以上、傾けられるはず)
    water_ratio = x / (a * b)

    # 答えを求める
    if water_ratio > 0.5:
        rad = math.atan2(a, 2 * (a * b - x) / a)
        ans = 90 - math.degrees(rad)

    else:
        rad = math.atan2(2 * x / b, b)
        ans = 90 - math.degrees(rad)

    print(ans)


# テストクラス
class TestClass(unittest.TestCase):
    def assertIO(self, assert_input, output):
        stdout, sat_in = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(assert_input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, sat_in
        self.assertEqual(out, output)

    def test_input_1(self):
        test_input = """2 2 4"""
        output = """45.0000000000"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """12 21 10"""
        output = """89.7834636934"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """3 1 8"""
        output = """4.2363947991"""
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
