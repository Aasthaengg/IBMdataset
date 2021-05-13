import sys
from io import StringIO
import unittest
import os
import itertools

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    n, k = map(int, input().split())

    if (n * (n - 1)) // 2 - (n - 1) < k:
        print(-1)
        return

    # 点の一覧(1~n)
    points = [i for i in range(1, n + 1)]

    # 辺の一覧(初期値：中心点から延びる辺の一覧)
    e = [(1, point) for point in points if not point == 1]
    # 辺の数
    cnt = len(e)

    # 増やせる辺の候補
    addables = itertools.combinations(points[1:], 2)

    # いくつ辺を追加するか
    # k= 6 = 増やさない。
    # k= 0 = 6回増やす。
    # つまり「(n * (n - 1)) / 2 - (n - 1) - k」だけ辺を増やす。
    adds = list(addables)[0:(n * (n - 1)) // 2 - (n - 1) - k]
    e += adds
    cnt += len(adds)

    print(cnt)

    for aa in e:
        print(str(aa[0]) + " " + str(aa[1]))


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
        test_input = """5 3"""
        output = """5
4 3
1 2
3 1
4 5
2 3"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """5 8"""
        output = """-1"""
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
