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
m = 0
b = []
cnt = [[] for _ in range(n+1)]
for i in range(1, n+1):
    j = i
    c = 1
    while j*c <= n:
        cnt[j*c].append(i)
        c += 1

tmp = [0]*(n+1)
for i in range(n)[::-1]:
    if tmp[i+1] % 2 != a[i]:
        b.append(i+1)
        m += 1
        for j in cnt[i+1]:
            tmp[j] += 1

if m == 0:
    print(m)
else:
    print(m)
    print(*b[::-1])
