import sys
from io import StringIO
import unittest
import os
import bisect

# 検索用タグ、尺取り、3つの内2つを固定
# https://drken1215.hatenablog.com/entry/2019/10/20/032700

# 実装を行う関数
def resolve():
    n = int(input())
    ls = list(map(int, input().split()))

    ls.sort()

    ans = 0
    # 尺取り
    for i in range(n - 2):
        a = ls[i]
        for j in range(i + 1, n - 1, 1):
            b = ls[j]
            # 以下がサンプル通りだが、TLE。
            # for k in range(j + 1, n, 1):
            #     c = ls[k]
            #     if not c < a + b:
            #         break
            #     ans += 1
            cnt = bisect.bisect_left(ls, a + b, j)
            ans += cnt - j - 1

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
        test_input = """4
3 4 2 1"""
        output = """1"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """3
1 1000 1"""
        output = """0"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """7
218 786 704 233 645 728 389"""
        output = """23"""
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
