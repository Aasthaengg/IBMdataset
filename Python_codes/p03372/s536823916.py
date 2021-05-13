#!/usr/bin/env python3
#ABC95 D

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

n,c = LI()
xv = [LI() for _ in range(n)]

l1 = [v for x,v in xv]
l2 = l1[:]
r1 = l1[::-1]
r2 = r1[:]

l1 = list(accumulate(l1))
l2 = list(accumulate(l2))
r1 = list(accumulate(r1))
r2 = list(accumulate(r2))

for i,(x,v) in enumerate(xv):
    l1[i] -= x
    l2[i] -= 2*x
    r1[-i-1] -= c - x
    r2[-i-1] -= 2*(c - x)

for i in range(1,n):
    l1[i] = max(l1[i],l1[i-1])
    r1[i] = max(r1[i],r1[i-1])

ans = max(l1[-1],r1[-1])
for i in range(n-1):
    ans = max(ans,l2[i] + r1[-i-2])
    ans = max(ans,r2[i] + l1[-i-2])
print(max(0,ans))