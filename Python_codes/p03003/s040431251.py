#!/usr/bin/env python3
#ABC130 E

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000)
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

n,m = LI()
s = LI()
t = LI()
dp  = [[0]*(m+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n+1):
    dp[i][0] = 1
for j in range(m+1):
    dp[0][j] = 1
for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j]) % mod
        else:
            dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) % mod
print(dp[n][m])