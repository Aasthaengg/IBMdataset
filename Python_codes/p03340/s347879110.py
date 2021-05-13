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
a = [0] + LI()
b = list(accumulate(a))
l,r,tmp,ans = 0,0,0,0
while r < n:
    if b[r+1] - b[l] == tmp ^ a[r+1]:
        tmp ^= a[r+1]
        r += 1
        ans += r-l
    elif l == r:
        tmp ^= a[l]
        l += 1
        r += 1
    else:
        l += 1
        tmp ^= a[l]
print(ans)
