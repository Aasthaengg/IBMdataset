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


n = input()
m = len(n)
n = n[::-1] + '0'

dp = [[inf]*2 for _ in range(m+1)]
dp[0][0] = 0
for i in range(m):
    x = int(n[i])
    for j in range(2):
        x += j
        for a in range(10):
            b = a-x
            if a >= x:
                dp[i+1][0] = min(dp[i+1][0],dp[i][j]+a+b)
            else:
                dp[i+1][1] = min(dp[i+1][1],dp[i][j]+a+10+b)
ans = min(dp[-1][0],dp[-1][1]+1)
print(ans)