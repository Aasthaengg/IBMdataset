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

n = I()
a = LI()
cnt = 0
for i in range(n):
    if a[i] < 0:
        cnt += 1

if cnt % 2:
    m = inf
    ans = 0
    for i in range(n):
        m = min(m, abs(a[i]))
        ans += abs(a[i])
    ans -= 2*m
    print(ans)
else:
    ans = 0
    for i in range(n):
        ans += abs(a[i])
    print(ans)