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

H, W, D = map(int ,input().split())

dict = {}
for i in range(1,H+1):
    A = [0] + list(map(int, input().split()))
    for j in range(1, W+1):
        dict[A[j]] = (i,j)

P = [[]]
for i in range(1,D+1):
    q = [0]
    k = i + D
    while k <= H*W:
        p = abs(dict[k][0] - dict[k-D][0]) + abs(dict[k][1] - dict[k-D][1])
        q.append(q[-1]+p)
        k = k + D
    P.append(q)

Q = int(input())

for i in range(Q):
    L, R = map(int, input().split())
    j = L % D
    if j == 0: j = D
    print(P[j][(R-1) // D] - P[j][(L-1) // D])
