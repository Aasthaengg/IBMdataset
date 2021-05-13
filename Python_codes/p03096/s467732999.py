#!/usr/bin/env python3
#AGC31 B

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000000)
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

n = I()
c = [I() for _ in range(n)]
dp1,dp2 = [0]*(n+1),[0]*(max(c)+1)
dp1[0] = 1
for i in range(n):
    if dp2[c[i]] == 0:
        dp1[i+1] = dp1[i]
        dp2[c[i]] = dp1[i]
        dp2[c[i]] %= mod
    else:
        if c[i] == c[i-1]:
            dp1[i+1] = dp1[i]
            continue
        dp1[i+1] += dp2[c[i]]
        dp1[i+1] += dp1[i]
        dp2[c[i]] += dp1[i]
        dp2[c[i]] %= mod
        dp1[i+1] %= mod
print(dp1[-1] % mod)
