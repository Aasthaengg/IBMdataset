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

n, m = LI()
lst = [[] for _ in range(n)]

for i in range(m):
    p, y = LI()
    lst[p-1].append([y, i])

for i in lst:
    i.sort()

ans = []
for i in range(n):
    for idx, [j, k] in enumerate(lst[i]):
        s = "0" * 6 + str(i+1)
        s = s[-6:]
        t = "0" * 6 + str(idx+1)
        t = t[-6:]
        ans.append([k, s+t])
ans.sort()
for i, j in ans:
    print(j)