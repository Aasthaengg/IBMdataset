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

N, x = map(int, input().split())
a = [0] + list(map(int, input().split()))

ans = 0
for i in range(1,N+1):
    y = a[i-1] + a[i]
    if y > x:
        ans += y-x
        a[i] -= y-x
print(ans)