import sys
import math
import fractions
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(10**7)

S = input()

dp = [[0] * 13 for _ in range(len(S))]
mod = 10 ** 9 + 7

if S[0] == '?':
    for i in range(10):
        dp[0][i] = 1
else:
    dp[0][int(S[0])] = 1

for i in range(1, len(S)):
    if S[i] == '?':
        for j in range(13):
            for k in range(10):
                dp[i][(j * 10 + k) % 13] += dp[i-1][j]
                dp[i][(j + 10 + k) % 13] %= mod
    else:
        for j in range(13):
            dp[i][(j * 10 + int(S[i])) % 13] += dp[i-1][j]
            dp[i][(j * 10 + int(S[i])) % 13] %= mod
print(dp[len(S) - 1][5])
