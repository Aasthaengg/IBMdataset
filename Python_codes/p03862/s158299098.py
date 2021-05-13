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

n, x = LI()
a = LI()
ans = 0
for i in range(n):
    if a[i] > x:
        ans += a[i] - x
        a[i] = x
    if i < n-1:
        if a[i] + a[i+1] > x:
            ans += (a[i] + a[i+1]) - x
            a[i+1] = x - a[i]
print(ans)