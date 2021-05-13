#!/usr/bin/env python3
#ABC58 D

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

n,m = LI()
x = LI()
y = LI()
x.sort()
y.sort()
tmpx,tmpy = 0,0
for i in range(n):
    tmpx += x[i]*i
    tmpx -= x[i]*(n-1-i)
for i in range(m):
    tmpy += y[i]*i
    tmpy -= y[i]*(m-1-i)
ans = tmpx*tmpy
ans %= mod
print(ans)
