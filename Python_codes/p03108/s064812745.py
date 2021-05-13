import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


class UnionFind:
    def __init__(self, n):
        """
        コンストラクタ
        :要素数 n:
        """
        self.n = n
        # 添字x: 値yとすると・・
        #   root以外の場合： 要素xは集合yに所属する。
        #   rootの場合　　　： 集合xの要素数はy個である。(負数で保持する)
        self.parents = [-1] * n

    def getroot(self, x):
        """
        所属する集合(ルートの番号)を取得する。
        :調査する要素 x:
        """
        # 値が負数 = ルートに到達したので、ルート木の番号を返す。
        if self.parents[x] < 0:
            return x
        else:
            # 値が正数 = ルートに到達していない場合、さらに親の情報を確認する。
            # 下の行は経路圧縮の処理。
            self.parents[x] = self.getroot(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        2つの要素が所属する集合をを同じ集合に結合する。
        :結合する要素(1つ目) x:
        :結合する要素(2つ目) y:
        """
        # 既に同じ集合に存在するなら何もせず終了。
        x = self.getroot(x)
        y = self.getroot(y)
        if x == y:
            return

        # 集合を結合する。
        # ※ここ、「要素数の大きい集合に、少ない集合を結合」しているが、こうすることで以後の「処理量を削減」するテクニックである。
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        指定した集合に属する要素数を取得する。
        :調査する集合 x:
        """
        # 添え字[root]には、要素数が負数で格納されている。そのため、取得する際は-反転する。
        return -self.parents[self.getroot(x)]

    def is_same(self, x, y):
        return self.getroot(x) == self.getroot(y)

    def members(self, x):
        """
        指定した集合に属する要素を取得する。size()と比較して速度が圧倒的に遅いので注意。
        :調査する集合 x:
        """
        root = self.getroot(x)
        return [i for i in range(self.n) if self.getroot(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


# 実装を行う関数
def resolve(test_def_name=""):
    n, m = map(int, input().split())
    ab_s = [list(map(int, input().split())) for i in range(m)]

    # uf 作成(要素数を+1しているのは添え字と島番号を合わせるため)
    uf = UnionFind(n + 1)
    convenient_val = [0 for i in range(m)]

    for cnt, ab in enumerate(reversed(ab_s)):
        if cnt > 0:

            size0 = uf.size(ab[0])
            size1 = uf.size(ab[1])
            if uf.is_same(ab[0], ab[1]):
                convenient_val[cnt] = convenient_val[cnt - 1] - (size0 * (size0 - 1) // 2)
            else:
                convenient_val[cnt] = convenient_val[cnt - 1] - (size0 * (size0 - 1) // 2) - (size1 * (size1 - 1) // 2)

        uf.union(ab[0], ab[1])

        convenient_val[cnt] += uf.size(ab[0]) * (uf.size(ab[0]) - 1) // 2

    convenient_val.reverse()

    for cnt, i in enumerate(convenient_val):
        if cnt == 0:
            continue

        print(convenient_val[0] - i)

    print(convenient_val[0])


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
        test_input = """4 5
1 2
3 4
1 3
2 3
1 4"""
        output = """0
0
4
5
6"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """6 5
2 3
1 2
5 6
3 4
4 5"""
        output = """8
9
12
14
15"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """2 1
1 2"""
        output = """1"""
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
