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
    A.append(list(map(int, input().split())))

A = sorted(A, key=lambda x: x[1])

t = 0
for i in range(N):
    t += A[i][0]
    if t > A[i][1]:
        print("No")
        sys.exit()

print("Yes")


