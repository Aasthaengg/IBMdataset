from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter,defaultdict
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)
# INF =  float("inf")
INF = 10**18
import bisect
import statistics
mod = 10**9+7
# mod = 998244353

N, Q = map(int, input().split())

events = []
for i in range(N):
    S, T, X = map(int, input().split())
    events.append([S-X-0.5, 1, X])
    events.append([T-X-0.5, -1, X])

for i in range(Q):
    d = int(input())
    events.append([d, 0, i])

events = sorted(events)

count = defaultdict(int)
Xheap = []
heapq.heapify(Xheap)
ans = [-1 for i in range(Q)]

for e in events:
    if e[1] == 1:
        heapq.heappush(Xheap, e[2])
        count[e[2]] += 1
    elif e[1] == -1:
        count[e[2]] -= 1
    else:
        while Xheap:
            a = Xheap[0]
            if count[a] == 0:
                heapq.heappop(Xheap)
            else:
                ans[e[2]] = a
                break

for i in range(Q):
    print(ans[i])