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
R, S, P = map(int, input().split())
T = input()

d = ["" for i in range(K)]
for i in range(N):
    d[i%K] += T[i]

def score(dd):
    c = 0
    if dd[0] == "r": c += P
    if dd[0] == "s": c += R
    if dd[0] == "p": c += S

    if len(dd) >= 1:
        flag = 0
        for i in range(1,len(dd)):
            if dd[i] == dd[i-1] and flag == 1:
                if dd[i] == "r": c += P
                if dd[i] == "s": c += R
                if dd[i] == "p": c += S
                flag = 0
            elif dd[i] == dd[i-1] and flag == 0:
                flag = 1
            elif dd[i] != dd[i-1]:
                if dd[i] == "r": c += P
                if dd[i] == "s": c += R
                if dd[i] == "p": c += S
                flag = 0

    return c

total = 0
for dd in d:
    total += score(dd)

print(total)
