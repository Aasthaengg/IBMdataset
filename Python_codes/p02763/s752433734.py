import sys
from io import StringIO
import unittest
import os


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    def segfunc(x, y):
        return x + y

    n = int(input())
    s = input()
    q = int(input())
    query_s = [list(input().split()) for i in range(q)]

    alpha2int = lambda c: ord(c) - 97

    sumcun = [[0 for a in range(n)] for i in range(26)]
    # 数え上げ実施
    for cnt, char in enumerate(list(s)):
        sumcun[alpha2int(char)][cnt] = 1

    # 各アルファベットが区間内で何回利用されているか、を保持するセグメントツリーを作成
    seg_s = [SegTree(sumcun[i], segfunc=segfunc, ide_ele=0) for i in range(26)]

    s_list = list(s)
    for query in query_s:
        if query[0] == "1":
            # 文字を変換
            target = int(query[1]) - 1  # 変換される文字の添え字
            # まず、変換される文字の利用回数。元々の値から-1減算
            target_tree = alpha2int(s_list[target])  # 操作するツリー
            seg_s[target_tree].update(target, 0)
            # 次に、変換後の文字の利用回数。元々の値に1を加算。
            target_tree = alpha2int(query[2])
            seg_s[target_tree].update(target, 1)
            # 文字列リストを置換しておく。(同じ位置の文字を再度書き換えるとき、s_list[添え字]で対象の文字を取得するため)
            s_list[target] = query[2]
        else:
            # 文字の種類を出力
            ans = 0
            # 各アルファベットに対して、以下の処理を実施。
            for i in range(26):
                # 先頭～対象範囲(from)の直前までに、文字が何個使用されているか取得。
                from_int = int(query[1])
                remove_cnt = 0
                if from_int > 1:
                    remove_cnt = seg_s[i].query(0, from_int - 1)
                # 先頭～対象範囲(to)のまでに、文字が何個使用されているか取得。
                to_int = int(query[2])
                all_cnt = seg_s[i].query(0, to_int)
                if all_cnt - remove_cnt > 0:
                    ans += 1
            print(ans)


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
        test_input = """7
abcdbbd
6
2 3 6
1 5 z
2 1 1
1 4 a
1 7 d
2 1 7"""
        output = """3
1
5"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """4
abcd
4
2 1 4
2 1 1
1 1 b
2 1 2
"""
        output = """4
1
1"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """4
abab
10
2 1 1
2 1 2
2 1 3
2 1 4
2 2 2
2 2 3
2 2 4
2 3 3
2 3 4
2 4 4
"""
        output = """1
2
2
2
1
2
2
1
2
1"""
        self.assertIO(test_input, output)

    def test_input_5(self):
        test_input = """78
xcajtlueygwtjfreordfpsmyvirremdzhsfisulnbmmkxkdrrkwtjhsfmltkoieuxtwnvvozgcoabm
16
1 25 e
1 32 m
1 36 f
1 38 r
1 40 w
1 40 e
1 46 o
1 49 l
1 53 e
1 57 t
1 58 j
1 64 z
1 70 a
1 73 t
1 74 j
2 27 78
"""
        output = """20"""
        self.assertIO(test_input, output)

    def test_input_6(self):
        test_input = """78
xcajtlueygwtjfreordfpsmyvirremdzhsfisulnbmmkxkdrrkwtjhsfmltkoieuxtwnvvozgcoabm
21
1 73 t
1 53 e
1 7 t
1 70 a
1 38 r
1 15 p
1 57 t
1 58 j
1 74 j
1 8 x
1 46 o
1 25 e
1 40 w
1 49 l
1 36 f
1 15 w
1 32 m
1 1 k
1 40 e
1 64 z
2 9 19
"""
        output = """10"""
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
