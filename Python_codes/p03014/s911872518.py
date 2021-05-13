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

H, W = map(int, input().split())

a = [[0 for j in range(W)] for i in range(H)]
b = [[0 for j in range(W)] for i in range(H)]

SS = []

for i in range(H):
    S = input() + "#"
    j = 0
    while j < W:
        if S[j] == "#":
            a[i][j] = 0
            j += 1
        else:
            count = 0
            k = j
            while S[k] == ".":
                count += 1
                k += 1
            for l in range(count):
                a[i][j+l] = count
            j = j + count
    SS.append(S)

SS.append("#"*(W+1))

for j in range(W):
    i = 0
    while i < H:
        if SS[i][j] == "#":
            b[i][j] = 0
            i += 1
        else:
            count = 0
            k = i
            while SS[k][j] == ".":
                count += 1
                k += 1
            for l in range(count):
                b[i+l][j] = count
            i = i + count

ans = 0
for i in range(H):
    for j in range(W):
        if ans < a[i][j] + b[i][j]:
            ans = a[i][j] + b[i][j]
print(ans-1)







