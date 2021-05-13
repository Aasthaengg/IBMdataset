import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


def prepare(n, mod=pow(10, 9) + 7):
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
    n, k = map(int, input().split())

    # 逆数を求める
    fns, invs = prepare(pow(10, 6))

    # 計算
    ans = 0
    for i in range(1, min(n - 1, k) + 1):
        # (fns[n] * invs[i] * invs[n - i]) 0の部屋パターン数
        # (fns[n - 1] * invs[i] * invs[n - 1 - i])  移動先数(重複組み合わせで求める。)
        ans += (fns[n] * invs[i] * invs[n - i]) * (fns[n - 1] * invs[i] * invs[n - 1 - i]) % (pow(10, 9) + 7)
        ans = ans % (pow(10, 9) + 7)

    # ALL1のパターンを考慮して+1した結果を出力。
    print(ans + 1)


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
        test_input = """3 2"""
        output = """10"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """200000 1000000000"""
        output = """607923868"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """15 6"""
        output = """22583772"""
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
