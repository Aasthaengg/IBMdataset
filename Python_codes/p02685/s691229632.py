import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


class youk_prepare:
    def __init__(self, n, mod=pow(10, 9) + 7):
        """
        コンストラクタ
        :n個の物に対する組み合わせを求める(200万くらいなら十分動く。1億とかは無理。)
        :余り mod
        """
        f = 1
        factorials = [1]
        for m in range(1, n + 1):
            f *= m
            f %= mod
            factorials.append(f)
        inv = pow(f, mod - 2, mod)
        invs = [1] * (n + 1)
        invs[n] = inv
        for m in range(n, 1, -1):
            inv *= m
            inv %= mod
            invs[m - 1] = inv

        # fn：1～nの階乗のリスト(mod結果) invs：0～nまでの数値の逆数のリスト
        self.factorials = factorials
        self.invs = invs
        self.mod = mod

    def cmb(self, n, r):
        """
        組み合わせ数を求める
        :n個の物からr個を選ぶ
        """
        if len(self.factorials) - 1 < n:
            raise ValueError("コンストラクタで指定した要素数を超えているので無理。")
        return (self.factorials[n] * self.invs[r] * self.invs[n - r]) % self.mod

    def multi_cmb(self, n, r):
        """
        重複組み合わせ数を求める
        :n種類のものから重複を許してr個選ぶ(例3職のボールから5つを選ぶ)
        """
        if len(self.factorials) - 1 < n:
            raise ValueError("コンストラクタで指定した要素数を超えているので無理。")
        return (self.factorials[n] * self.invs[r] * self.invs[n - r]) * (
                self.factorials[n - 1] * self.invs[r] * self.invs[n - 1 - r]) % self.mod


def prepare(n, mod=998244353):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= mod
        factorials.append(f)
    inv = pow(f, mod - 2, mod)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= mod
        invs[m - 1] = inv

    return factorials, invs


# 実装を行う関数
def resolve(test_def_name=""):
    n, m, k = map(int, input().split())

    # 全組み合わせ数(重複順列)
    # all_pattern = pow(m, n, 998244353)

    prepare = youk_prepare(200000, 998244353)
    # 使用方法サンプル(10 N 3= 10個の要素から3つを選ぶ場合の組み合わせ数)
    # fns, invs = prepare(200000)

    # さらに6 N 5= 6個の要素から5つを選ぶ場合の組み合わせ数 ->このように、大量のパターンが欲しいときはこっちを使う。
    # aa = (fns[6] * invs[5] * invs[6 - 5]) % 998244353  # ans=120

    # 許容される組み合わせを加算していく
    ans = 0
    for i in range(k + 1):
        # ans += (m * pow(m - 1, m - i - 1, 998244353) * cmb(n - 1, i)) % 998244353
        # ans = (fns[n-1] * invs[k] * invs[n-1 - k]) % 998244353
        # ans += m * pow(m - 1, n - i - 1, 998244353) * (fns[n - 1] * invs[i] * invs[n - 1 - i])
        ans += m * pow(m - 1, n - i - 1, 998244353) * prepare.cmb(n - 1, i)
        ans = ans % 998244353

    print(ans)

    # ans = (m * pow(m - 1, m - k - 1, 998244353) * cmb(n - 1, k)) % 998244353

    # カウント外の組み合わせ数
    # kpl1 = k + 1
    # ng_pattern = m * pow((m - 1), n - (k + 1), 998244353)
    # ng_pattern = ng_pattern % 998244353
    # ans = all_pattern - ng_pattern


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
        test_input = """3 2 1"""
        output = """6"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """100 100 0"""
        output = """73074801"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """60522 114575 7559"""
        output = """479519525"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def test_1original_1(self):
        test_input = """4 10 0"""
        output = """7290"""
        self.assertIO(test_input, output)

    def test_1original_2(self):
        test_input = """4 10 1"""
        output = """9720"""
        self.assertIO(test_input, output)

    def test_1original_3(self):
        test_input = """4 10 2"""
        output = """9990"""
        self.assertIO(test_input, output)

    def test_1original_4(self):
        test_input = """4 10 3"""
        output = """10000"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()