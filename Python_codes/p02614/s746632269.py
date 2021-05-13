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

H, W, K = map(int, input().split())
c = []
for i in range(H):
    c.append(list(input()))

def bit(S, j):
    # Sの右からj bit目(0-indexed)
    return (S>>j)&1

ans = 0
for i in range(1<<H):
    for j in range(1<<W):
        cc = copy.deepcopy(c)
        black = 0
        for ki in range(H):
            for kj in range(W):
                if bit(i,ki) == 1:
                    cc[ki] = ["r" for _ in range(W)]
                if bit(j,kj) == 1:
                    for ii in range(H):
                        cc[ii][kj] = "r"

        for ii in range(H):
            for jj in range(W):
                if cc[ii][jj] == "#":
                    black += 1

        if black == K:
            ans += 1

print(ans)












