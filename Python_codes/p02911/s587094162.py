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

N, K, Q = map(int, input().split())

g = [0 for i in range(N)]

for i in range(Q):
    A = int(input())
    g[A-1] += 1

for i in range(N):
    if Q - g[i] >= K:
        print("No")
    else:
        print("Yes")

