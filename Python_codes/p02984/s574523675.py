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
A = list(map(int, input().split()))

ans = []
a1 = 0
for i in range(N):
    a1 += (-1)**i*A[i]

ans.append(a1)

a = a1//2
for i in range(N-1):
    a = A[i] - a
    ans.append(2*a)

ans = map(str, ans)
print(" ".join(ans))


