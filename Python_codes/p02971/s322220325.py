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

A = []
for i in range(N):
    A.append(int(input()))

AA = Counter(A)

B = sorted(AA.items(), key=lambda x:x[0])

if B[-1][1] == 1:
    c = B[-2][0]
else:
    c = B[-1][0]

M = B[-1][0]

for i in range(N):
    if A[i] == M:
        print(c)
    else:
        print(M)


