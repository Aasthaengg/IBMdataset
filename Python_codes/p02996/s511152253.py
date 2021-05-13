import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    # 数値取得サンプル
    n = int(input())
    a_b = [list(map(int, input().split())) for i in range(n)]
    a_b = sorted(a_b, key=lambda x: x[1])

    time_space = 0
    for i in range(len(a_b)):
        if i == 0:
            time_space = a_b[i][1] - a_b[i][0]
        else:
            time_space = a_b[i][1] - a_b[i - 1][1] - a_b[i][0] + time_space

        if time_space < 0:
            print("No")
            return

    print("Yes")


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
        test_input = """5
2 4
1 9
1 8
4 9
3 12"""
        output = """Yes"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """3
334 1000
334 1000
334 1000"""
        output = """No"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """30
384 8895
1725 9791
170 1024
4 11105
2 6
578 1815
702 3352
143 5141
1420 6980
24 1602
849 999
76 7586
85 5570
444 4991
719 11090
470 10708
1137 4547
455 9003
110 9901
15 8578
368 3692
104 1286
3 4
366 12143
7 6649
610 2374
152 7324
4 7042
292 11386
334 5720"""
        output = """Yes"""
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
