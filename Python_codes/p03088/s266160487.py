import os
import re
import sys
from collections import defaultdict

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

N = int(sys.stdin.buffer.readline())


def is_ok(s):
    ok = True
    for ng in ['AGC', 'GAC', 'ACG']:
        ok &= ng not in s
    ok &= not re.match(r'A.GC', s)
    ok &= not re.match(r'AG.C', s)
    return ok


# 最後が s である文字の数
dp = [defaultdict(int) for _ in range(N)]
for c in 'AGCT':
    for d in 'AGCT':
        for e in 'AGCT':
            if is_ok(c + d + e):
                dp[2][c + d + e] = 1

for i in range(3, N):
    for k in dp[i - 1].keys():
        for c in 'AGCT':
            if is_ok(k + c):
                dp[i][k[-2:] + c] += dp[i - 1][k]
                dp[i][k[-2:] + c] %= MOD

print(sum(dp[-1].values()) % MOD)
