import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

def main():
    a, b, c, d, e, f = ns()
    max_cncnt, ans_sum, ans_sugar = -1, 0, 0

    sugar_cand = []
    sugar_dp = [False for _ in range(f + 1)]
    sugar_dp[0] = True
    for i in range(f + 1):
        if sugar_dp[i]:
            if i + c <= f:
                sugar_dp[i + c] = True
            if i + d <= f:
                sugar_dp[i + d] = True
            sugar_cand.append(i)

    for i in range(f // (100 * a) + 1):
        for j in range(f // (100 * b) + 1):
            water = 100 * (a * i + b * j)
            if water == 0:
                continue
            if water > f:
                break
            sugar_lim = min(water * e // 100, f - water)
            sugar_idx = bisect.bisect_right(sugar_cand, sugar_lim)
            sugar = 0 if sugar_idx == 0 else sugar_cand[sugar_idx - 1]
            if max_cncnt < sugar / (water + sugar):
                ans_sum = water + sugar
                ans_sugar = sugar
                max_cncnt = ans_sugar / ans_sum

    print(ans_sum, ans_sugar)


if __name__ == '__main__':
    main()
