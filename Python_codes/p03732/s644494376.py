# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

N, W = MAP()
WV = []
for i in range(N):
    w, v = MAP()
    WV.append((w, v))

dp = [defaultdict(int) for i in range(N+1)]
dp[0][0] = 0
for i in range(N):
    w, v = WV[i]
    for k in dp[i].keys():
        dp[i+1][k] = max(dp[i+1][k], dp[i][k])
        if k+w <= W:
            dp[i+1][k+w] = max(dp[i+1][k+w], dp[i][k] + v)
print(max(dp[N].values()))