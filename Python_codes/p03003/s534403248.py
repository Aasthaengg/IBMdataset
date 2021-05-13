import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

MOD = 10**9 + 7

N,M = map(int,readline().split())
S = list(map(int,readline().split()))
T = np.array(['0']+readline().split(),np.int32)

# Sは左から見ていく。
# Tについて、（最後に一致させた文字の位置、通り数）をdpで持つ

dp = np.zeros(M+1,dtype=np.int64)
dp[0] = 1

for i,s in enumerate(S,1):
    prev = dp
    prev_cum = prev.cumsum() % MOD
    equal = (s == T)
    dp[1:] += equal[1:] * prev_cum[:-1]
    dp[dp>=MOD] -= MOD

answer = dp.sum() % MOD
print(answer)