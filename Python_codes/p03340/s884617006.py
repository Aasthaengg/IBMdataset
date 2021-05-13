#!/usr/bin/env python3
#ARC98 D

import sys
import math
import bisect
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
a = LI()
l,r,tmp,ans = 0,0,0,0
while l < n and r < n:
    while tmp & a[r] == 0:
        tmp += a[r]
        r += 1
        ans += r - l
        if r == n:
            break
    if l == r:
        tmp += a[r]
        r += 1
    tmp -= a[l]
    l += 1
print(ans)
