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

N, M = map(int, input().split())
A = list(map(lambda x: -x, list(map(int, input().split()))))

heapq.heapify(A)

for i in range(M):
    a = -heapq.heappop(A)
    a = a // 2
    heapq.heappush(A, -a)

print(-sum(A))

