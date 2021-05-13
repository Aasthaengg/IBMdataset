#!/usr/bin/env python3
#ABC54 D

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7

n,ma,mb = map(int,input().split())
x = [list(map(int,input().split())) for _ in range(n)]
sa = 0
sb = 0
for a,b,c in x:
    sa += a
    sb += b
dp = [[float('inf')]*(sb+1) for _ in range(sa+1)]
dp[0][0] = 0
for a,b,c in x:
    y = [[True]*(sb+1) for _ in range(sa+1)]
    for i in range(sa+1-a):
        for j in range(sb+1-b):
            if y[i][j]:
                if dp[i+a][j+b] > dp[i][j] + c:
                    dp[i+a][j+b] = dp[i][j] + c
                    y[i+a][j+b] = False
ans = float('inf')
for i in range(1,sa+1):
    for j in range(1,sb+1):
        if i*mb == j*ma:
            ans = min(ans,dp[i][j])
if ans == float('inf'):
    print(-1)
else:
    print(ans)
