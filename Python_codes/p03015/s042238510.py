#!/usr/bin/env python3

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

l = input()
L = len(l)

dp1 = [0]*(L+1) #未満
dp2 = [0]*(L+1) #以下
dp1[0] = 1
dp2[0] = 0
for i in range(L):
    if l[i] == '1':
        dp1[i+1] += dp1[i]*2
        dp1[i+1] %= mod
        dp2[i+1] += dp1[i]
        dp2[i+1] %= mod
        dp2[i+1] += dp2[i]*3
        dp2[i+1] %= mod
    else:
        dp1[i+1] += dp1[i]
        dp1[i+1] %= mod
        dp2[i+1] += dp2[i]*3
        dp2[i+1] %= mod

ans = dp1[-1] + dp2[-1]
ans %= mod
print(ans)