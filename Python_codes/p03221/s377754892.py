import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    # 数値取得サンプル
    #   1行1項目 n = int(input())
    #   1行2項目 x, y = map(int, input().split())
    #   1行N項目 x = list(map(int, input().split()))
    #   N行1項目 x = [int(input()) for i in range(n)]
    #   N行N項目 x = [list(map(int, input().split())) for i in range(n)]

    # 文字取得サンプル
    #   1行1項目 x = input()
    #   1行1項目(1文字ずつリストに入れる場合) x = list(input())
    n, m = map(int, input().split())
    py_s = [list(map(int, input().split())) for i in range(m)]


    num = 0
    city = 0
    city_str = ""
    numdict = {}

    for i in sorted(py_s, key=lambda x: [x[0], int(x[1])]):
        if city != i[0]:
            city = i[0]
            city_str = format(city, '06')
            num = 0
        num += 1
        numdict[i[1]] = "".join([city_str, format(num, '06')])

    for i in py_s:
        print(numdict[i[1]])


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
        test_input = """2 3
1 32
2 63
1 12"""
        output = """000001000002
000002000001
000001000001"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """2 3
2 55
2 77
2 99"""
        output = """000002000001
000002000002
000002000003"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def test_original1(self):
        test_input = """100000 4
100000 1000000000
2 1
2 10
2 2
"""
        output = """100000000001
000002000001
000002000003
000002000002"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def t_est_original2(self):
        test_input = """4 1
1 20
"""
        output = """000001000001"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
