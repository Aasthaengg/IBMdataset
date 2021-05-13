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
    m = int(input())
    b_s = list(map(int, input().split()))

    divisors = [[0]] + [make_divisors(i) for i in range(1, m + 1)]
    ans = [0] + [0 for i in range(1, m + 1)]
    count = [0] + [0 for i in range(1, m + 1)]

    for num, b in reversed(list(enumerate(b_s, start=1))):
        if (b == 1 and count[num] % 2 == 0) or (b == 0 and count[num] % 2 != 0):
            ans[num] = 1
            for div in divisors[num]:
                count[div] += 1

    # 結果比較
    # if b_s != ans:
    #     print(-1)
    #     return
    ans = ans[1:]
    print(ans.count(1))

    if ans.count(1) == 0:
        return

    aaa = []
    for cnt, i in enumerate(ans, start=1):
        if i == 1:
            aaa.append(cnt)

    print(*aaa)

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
1 0 0"""
        output = """1
1"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """5
0 0 0 0 0"""
        output = """0"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """5
1 0 0 0 1"""
        output = """1
5"""
        self.assertIO(test_input, output)

    def test_input_4(self):
        test_input = """5
0 0 0 0 1"""

        output = """2
1 5"""
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
