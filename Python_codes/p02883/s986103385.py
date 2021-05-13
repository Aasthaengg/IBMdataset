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
A = sorted(list(map(int, input().split())))
F = sorted(list(map(int, input().split())), reverse=True)

ng = -1
ok = 10**12 + 1

def is_ok(m):
    FF = [m//f for f in F]
    p = 0
    for i in range(len(A)):
        p += max(0, A[i] - FF[i])
    if K >= p:
        return True
    else:
        return False

while (abs(ok-ng)>1):
    mid = (ng + ok) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)