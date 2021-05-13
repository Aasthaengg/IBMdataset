import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    # 数値取得サンプル
    n, k = map(int, input().split())
    s_s = list(input())

    if len(s_s) == 1:
        print(0)
        return

    # 処理
    target = []
    actcnt = 0
    for cnt, s in enumerate(s_s[1:], start=1):
        if actcnt == k:
            break
        bef_str = s_s[cnt - 1]

        if bef_str != s:
            target.append(cnt)
        if len(target) == 2:
            for work in range(target[0], target[1]):
                s_s[work] = "L" if s_s[work] == "R" else "R"
            target = []
            actcnt += 1
        if len(target) == 1 and cnt == len(s_s) - 1:
            for work in range(target[0], len(s_s)):
                s_s[work] = "L" if s_s[work] == "R" else "R"

    # 処理後、要素を数え上げる。
    ans = 0
    for cnt, s in enumerate(s_s[1:], start=1):
        bef_str = s_s[cnt - 1]
        if bef_str == s:
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
        test_input = """6 1
LRLRRL"""
        output = """3"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """13 3
LRRLRLRRLRLLR"""
        output = """9"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """10 1
LLLLLRRRRR"""
        output = """9"""
        self.assertIO(test_input, output)

    def test_input_4(self):
        test_input = """9 2
RRRLRLRLL"""
        output = """7"""
        self.assertIO(test_input, output)

    def test_input_5(self):
        test_input = """1 2
R"""
        output = """0"""
        self.assertIO(test_input, output)

    def test_input_6(self):
        test_input = """10 2
LLLLLRLRLL"""
        output = """9"""
        self.assertIO(test_input, output)

    def test_input_7(self):
        test_input = """10 2
LLLLLRLRLR"""
        output = """8"""
        self.assertIO(test_input, output)

    def test_input_8(self):
        test_input = """10 1
RLLLLRLRLR"""
        output = """5"""
        self.assertIO(test_input, output)

    def test_input_9(self):
        test_input = """10 1000
LLLLLRLRLL"""
        output = """9"""
        self.assertIO(test_input, output)

    def test_input_9(self):
        test_input = """10 1000
LLLLLLLLLL"""
        output = """9"""
        self.assertIO(test_input, output)

    def test_input_10(self):
        test_input = """10 1
RLLLRLLLLR"""
        output = """7"""
        self.assertIO(test_input, output)

        test_input = """10 2
RLRLRLRLRL"""
        output = """4"""
        self.assertIO(test_input, output)

        test_input = """10 3
RLRLRLRLRL"""
        output = """6"""
        self.assertIO(test_input, output)

        test_input = """10 4
RLRLRLRLRL"""
        output = """8"""
        self.assertIO(test_input, output)

        test_input = """10 5
RLRLRLRLRL"""
        output = """9"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def test_input_11(self):
        test_input = """10 5
RLRLRLRLRL"""
        output = """9"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
