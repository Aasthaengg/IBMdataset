import sys
from io import StringIO
import unittest
import os
import heapq

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    # 数値取得サンプル
    n, m = map(int, input().split())
    a_s = list(map(int, input().split()))
    bc_s = [list(map(int, input().split())) for i in range(m)]

    # 優先度付きキューの作成
    a_que = []
    heapq.heapify(a_que)
    b_que = []
    heapq.heapify(b_que)

    # (値,使用回数)setをキューに追加
    for a in a_s:
        heapq.heappush(a_que, a)
    for bc in bc_s:
        heapq.heappush(b_que, (-bc[1], bc[0]))

    ans = []
    now_b = 0
    choise_cnt = 0
    for i in range(m):

        now_b, b_cnt = heapq.heappop(b_que)
        now_b = -now_b

        for j in range(b_cnt):
            if choise_cnt >= n or len(a_que) == 0:
                break
            now_a = heapq.heappop(a_que)
            if now_b >= now_a:
                ans.append(now_b)
                choise_cnt += 1

    # ans = 採用するbの値の一覧
    a_s = sorted(a_s, reverse=True)
    for i in range(n - choise_cnt):
        ans.append(a_s[i])

    print(sum(ans))


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
        test_input = """3 2
5 1 4
2 3
1 5"""
        output = """14"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """10 3
1 8 5 7 100 4 52 33 13 5
3 10
4 30
1 4"""
        output = """338"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """3 2
100 100 100
3 99
3 99"""
        output = """300"""
        self.assertIO(test_input, output)

    def test_input_4(self):
        test_input = """11 3
1 1 1 1 1 1 1 1 1 1 1
3 1000000000
4 1000000000
3 1000000000"""
        output = """10000000001"""
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
