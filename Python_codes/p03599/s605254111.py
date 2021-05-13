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

a, b, c, d, e, f = LI()

x = f // (100*a)
y = f // (100*b)

max_ = -1
max__ = 1
for i in range(x + 1):
    for j in range(y + 1):
        E = min((a*i + b*j) * e, f - (100*a*i + 100*b*j))
        min_ = inf
        for k in range(E // c + 1):
            for l in range(E // d + 1):
                if c*k + d*l > E:
                    continue
                min_ = min(min_, E - c*k - d*l)
        E -= min_
        if max_ * (a*i + b*j) < E * max__:
            max_ = E
            max__ = a*i + b*j
            ans1 = (a*i + b*j) * 100 + E
            ans2 = E
print(ans1, ans2)