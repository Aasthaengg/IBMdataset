import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


# 実装を行う関数
def resolve(test_def_name=""):
    # 数値取得サンプル

    #   N行N項目 x = [list(map(int, input().split())) for i in range(n)]

    # 文字取得サンプル
    #   1行1項目 x = input()

    a, b = map(int, input().split())

    a = make_divisors(a)
    b = make_divisors(b)

    # 公約数 = 一致する値。
    a_b_divisor = list(set(a) & set(b))

    a_b_divisor.sort()

    if len(a_b_divisor) <= 1:
        print(len(a_b_divisor))
        return

    # エラストテネスの篩
    aa = -1
    for i in a_b_divisor[1:]:
        if len(a_b_divisor) <= 1:
            break

        if i > a_b_divisor[-1] / 2:
            break

        aa += 1
        sieve = i

        new_list = []

        for j in a_b_divisor:
            if j <= i or not j % sieve == 0:
                new_list.append(j)

        a_b_divisor = new_list

    print(len(a_b_divisor))

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
        test_input = """12 18"""
        output = """3"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """420 660"""
        output = """4"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """1 2019"""
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
