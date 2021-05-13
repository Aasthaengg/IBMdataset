from itertools import groupby
from collections import defaultdict

mod = 10**9+7
N = int(input())
C = [int(input()) for _ in range(N)]
C = [k for k, g in groupby(C)]
num = defaultdict(int)
dp = [1] + [0] * len(C)
for i, c in enumerate(C):
    dp[i+1] = num[c] = (dp[i] + num[c]) % mod
print(dp[-1])