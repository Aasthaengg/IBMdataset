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

N, K = map(int, input().split())
V = list(map(int, input().split()))

m = 0
for i in range(1, K+1):
    if i <= N:
        for j in range(1,i+1):
            VV = deque(copy.deepcopy(V))
            a = []
            heapq.heapify(a)
            for k in range(j):
                v = VV.popleft()
                heapq.heappush(a,v)
            for k in range(i-j):
                v = VV.pop()
                heapq.heappush(a, v)
            ans = sum(a)
            for k in range(K-i):
                if len(a) > 0:
                    v = heapq.heappop(a)
                    if v < 0:
                        ans -= v
            m = max(m,ans)
    else:
        ans = sum(V)
        a = copy.deepcopy(V)
        heapq.heapify(a)
        for k in range(K-N):
            if len(a) > 0:
                v = heapq.heappop(a)
                if v < 0:
                    ans -= v
        m = max(m, ans)
        break

print(m)




