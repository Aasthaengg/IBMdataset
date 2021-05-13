import sys
from io import StringIO
import unittest
import os

sys.setrecursionlimit(999999999)


def dfs(now, edge, colors):
    # 枝を全て調査
    for i in edge[now]:
        # 色を設定済みなら何もしない
        if not colors[i[0]] == -1:
            continue

        # 色の設定
        # 親子の距離%2(偶数0:奇数:1) + 親(偶数0:奇数:1) の余りを子に設定(偶数なら0 奇数なら1を設定できるロジック)
        colors[i[0]] = (i[1] % 2 + colors[now]) % 2

        # 再帰処理
        dfs(i[0], edge, colors)


# 実装を行う関数
def resolve():
    n = int(input())
    uvw = [list(map(int, input().split())) for i in range(n - 1)]

    edge = [[] for i in range(n + 1)]

    # 例：edge[0] = [[1, 100][2, 300]]
    # 点0は点1と距離100、点2と距離300でつながっている。
    for i in uvw:
        edge[i[0]].append([i[1], i[2]])
        edge[i[1]].append([i[0], i[2]])

    # -1は「未設定」の意味
    colors = [-1 for i in range(n + 1)]

    # 初期(適当な点を黒に塗る)
    colors[1] = 1

    dfs(1, edge, colors)

    for i in range(1, len(colors)):
        print(colors[i])


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
        test_input = """3
1 2 2
2 3 1"""
        output = """0
0
1"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """5
2 5 2
2 3 10
1 3 8
3 4 2"""
        output = """1
0
1
0
1"""
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
