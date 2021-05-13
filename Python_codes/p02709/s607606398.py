#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

"""
参考にしました(写経)
https://atcoder.jp/contests/abc163/submissions/12137623

Axが大きい順に置ける部分の中で一番左か一番右に置きたい
dp[i][j]:左からi個目, 右からj個目まで埋まっているときの最大値
i個目を見ているとき左と右に埋まっている数はi-1個なので
dp[i][j]は(左の個数,右の個数) = (0,i-1),(1,i-2),...とO(N)で探索できる
"""
n = I()
a = LI()
b = [[a[i],i] for i in range(n)]
b.sort(reverse=1)
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    a,j = b[i]
    for k in range(i+1):
        dp[k][i+1-k] = max(dp[k][i+1-k], dp[k][i-k] + a*abs(j-((n-1)-(i-k)))) #右側に追加
        dp[k+1][i-k] = max(dp[k+1][i-k], dp[k][i-k] + a*abs(j-k)) #左側に追加
ans = 0
for i in range(n):
    ans = max(ans, dp[i][n-i])
print(ans)