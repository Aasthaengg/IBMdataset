import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    n = int(input())
    a_s = list(map(int, input().split()))

    ans = [0]
    for i in range(n - 1):
        ans.append((a_s[i] * 2) - ans[i])

    add = a_s[-1] - ans[-1] // 2

    ans = [add]
    for i in range(n - 1):
        ans.append((a_s[i] * 2) - ans[i])

    print(*ans)


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
        test_input = """3
2 2 4"""
        output = """4 0 4"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """5
3 8 7 5 5"""
        output = """2 4 12 2 8"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """3
1000000000 1000000000 0"""
        output = """0 2000000000 0"""
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
