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


N = int(input())
s = defaultdict(int)

for i in range(N):
    s[input()] += 1

M = int(input())
t = defaultdict(int)
for i in range(M):
    t[input()] += 1

m = 0
for p in list(s.keys()):
    m = max(m, s[p] - t[p])
print(m)
