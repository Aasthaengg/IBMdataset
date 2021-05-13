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

d, g = LI()
pc = [LI() for _ in range(d)]

ans = inf
for i in range(1<<d):
    rest = 1
    rest_count = 0
    score = 0
    count = 0
    for j in range(d):
        p, c = pc[j]
        if (i >> j) & 1:
            score += p * (j + 1) * 100 + c
            count += p
        else:
            if rest < (j + 1) * 100:
                rest = (j + 1) * 100
                rest_count = p
    if score >= g:
        ans = min(ans, count)
    else:
        if math.ceil((g - score) / rest) <= rest_count:
            count += math.ceil((g - score) / rest)
            ans = min(ans, count)
print(ans)