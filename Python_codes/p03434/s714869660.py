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
a = list(map(int, input().split()))

a = sorted(a, reverse=True)

x = 0
y = 0
for i in range(len(a)):
    if i % 2 == 0:
        x += a[i]
    else:
        y += a[i]

print(x-y)
