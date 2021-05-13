import sys
from io import StringIO
import unittest
import os
import copy

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


# 実装を行う関数
def resolve(test_def_name=""):
    n = int(input())
    a_s = list(map(int, input().split()))

    input_fact_s = []
    need_s = {}
    # 最小公倍数(素因数)割り出し
    for a in a_s:
        aaa = factorization(a)
        input_fact_s.append(aaa)
        for fact in aaa:
            need_s[fact[0]] = max(fact[1], need_s.get(fact[0], 0))
    lcm = 1
    for val, cnt in need_s.items():
        lcm = (lcm * pow(val, cnt))

    ans = 0
    for a in a_s:
        ans += lcm // a

    print(ans % (pow(10, 9) + 7))

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
2 3 4"""
        output = """13"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """5
12 12 12 12 12"""
        output = """5"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """3
1000000 999999 999998"""
        output = """996989508"""
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
