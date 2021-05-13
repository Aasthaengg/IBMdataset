import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    l_s = list(input())
    ans = 0
    target = 0

    one_cnt = 0
    ans = 0
    for cnt, l in enumerate(l_s, 1):

        if l == "1":
            # これを、上位桁の1の個数×2パターン作成できる。
            pattern1 = pow(2, one_cnt, 1000000007)
            # 該当桁より後ろのパターン = 3^残り桁数乗
            pattern0 = pow(3, len(l_s) - cnt, 1000000007)

            ans += pattern0 * pattern1 % 1000000007
            one_cnt += 1

    # これを、上位桁の1の個数×2パターン作成できる。
    pattern1 = pow(2, one_cnt, 1000000007)
    # 該当桁より後ろのパターン = 3^残り桁数乗
    pattern0 = pow(3, 0, 1000000007)
    ans += pattern0 * pattern1 % 1000000007

    print(ans % 1000000007)


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
        test_input = """10"""
        output = """5"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """1111111111111111111"""
        output = """162261460"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
