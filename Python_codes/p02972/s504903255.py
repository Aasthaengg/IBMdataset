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
a = [0] + list(map(int, input().split()))

b = [0 for i in range(N+1)]
c = []
for i in range(N,0,-1):
    ii = 2*i
    s = 0
    while ii <= N:
        s += b[ii]
        ii += i
    s = s % 2
    if s == a[i]:
        b[i] = 0
    else:
        b[i] = 1
        c.append(i)

print(len(c))
if len(c) > 0:
    c = map(str, c)
    print(" ".join(c))
