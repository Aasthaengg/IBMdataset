import sys
from io import StringIO
import unittest
import os


# 検索用タグ、末尾に続く0の個数、ググる数学問題
# 実装を行う関数
def resolve(test_def_name=""):
    # 数値取得サンプル
    n = int(input())

    if n % 2 == 1:
        print(0)
        return

    ans = 0
    val = 2
    # ループ数に意味はない
    for i in range(30):
        val = val * 5
        if val > n:
            break
        ans += n // val

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
        test_input = """12"""
        output = """1"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """5"""
        output = """0"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """1000000000000000000"""
        output = """124999999999999995"""
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
