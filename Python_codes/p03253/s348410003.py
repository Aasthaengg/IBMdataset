import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


def cmb(n, r):
    mod = 10 ** 9 + 7
    ans = 1
    for i in range(r):
        ans *= n - i
        ans %= mod
    for i in range(1, r + 1):
        ans *= pow(i, mod - 2, mod)
        ans %= mod
    return ans


# 実装を行う関数
def resolve(test_def_name=""):
    n, m = map(int, input().split())

    if n == 1 or m == 1:
        print(1)
        return

    # ターゲットを素因数分解
    factor_list = factorization(m)

    ans = 1
    for i in factor_list:
        ans = ans * cmb((n - 1) + i[1], i[1])
        ans = ans % (pow(10, 9) + 7)

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
        test_input = """2 6"""
        output = """4"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """3 12"""
        output = """18"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """100000 1000000000"""
        output = """957870001"""
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
