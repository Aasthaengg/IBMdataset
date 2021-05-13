#!/usr/bin/env python3
#ABC128 E

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

n,q = LI()
stx = [LI() for _ in range(n)]
d = [I() for _ in range(q)]
stx.sort(key = lambda x:(x[2],x[0]))
ans = [-1]*q
skip = [-1]*q
for s,t,x in stx:
    l = bl(d,s-x)
    r = bl(d,t-x)
    while l < r:
        if ans[l] < 0:
            skip[l] = r
            ans[l] = x
            l += 1
        else:
            l = skip[l]
print(*ans)

