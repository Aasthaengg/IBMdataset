import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

N, K = list(map(int, sys.stdin.buffer.readline().split()))
A = list(map(int, sys.stdin.buffer.readline().split()))

A = np.array(A, dtype=int)
if K == 0:
    print(A.sum())
    exit()

# 各桁は独立に決まるので
# ビットが多く立ってる方を採用する
# d = 1
# ans = 0
# while d < 10 ** 13:
#     cnt1 = np.count_nonzero(A & d)
#     cnt0 = N - cnt1
#     ans += d * max(cnt1, cnt0)
#     d <<= 1
# print(ans)

DIGIT = (10**12).bit_length() + 1
# dp[d][s]:
# 上から DIGIT - d 桁目まで決めたときの最大値
# s = 0 のとき K より小さいことが確定した
dp = np.zeros((DIGIT, 2), dtype=int)
dp[0][1] = 0
dp[0][0] = -IINF

for d in range(1, DIGIT):
    mask = 1 << (DIGIT - d - 1)
    cnt0 = np.count_nonzero(A & mask)
    cnt1 = N - cnt0
    s0 = mask * cnt0
    s1 = mask * cnt1

    dp[d][0] = dp[d - 1][0] + max(s0, s1)
    if K & mask:
        # どっちも使える
        dp[d][1] = max(dp[d][1], dp[d - 1][1] + s1)
        dp[d][0] = max(dp[d][0], dp[d - 1][1] + s0)
    else:
        dp[d][1] = max(dp[d][1], dp[d - 1][1] + s0)
print(dp.max())


# def test():
#     ret = 0
#     for k in range(K + 1):
#         ret = max(ret, (A ^ k).sum())
#     print(ret)
#
#
# test()
