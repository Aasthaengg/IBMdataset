import itertools
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

H, W, K = list(map(int, sys.stdin.buffer.readline().split()))
K -= 1

if W == 1:
    print(1)
    exit()

valid_patterns = []
for pattern in itertools.product([True, False], repeat=W - 1):
    ok = True
    for a, b in zip(pattern, pattern[1:]):
        ok &= not (a and b)
    if ok:
        valid_patterns.append(pattern)
through = [0] * W
for pattern in valid_patterns:
    through[0] += pattern[0] is False
    through[-1] += pattern[-1] is False
    for i, (l, r) in enumerate(list(zip(pattern, pattern[1:]))):
        through[i + 1] += not l and not r

# dp[h][w]: 高さ h の左から w 番目の位置に来れるパターン数
dp = np.zeros((H + 1, W), dtype=int)
dp[0][0] = 1
for h in range(1, H + 1):
    dp[h] = dp[h - 1] * through % MOD
    for pattern in valid_patterns:
        for w, p in enumerate(pattern):
            if p:
                dp[h][w] += dp[h - 1][w + 1]
                dp[h][w + 1] += dp[h - 1][w]
        dp[h] %= MOD
print(dp[-1][K] % MOD)
