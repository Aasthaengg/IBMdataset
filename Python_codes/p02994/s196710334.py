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

N, L = map(int, input().split())

A = [L+i-1 for i in range(1,N+1)]

if 0 in A:
    print(sum(A))
else:
    AA = [abs(a) for a in A]
    b = min(AA)
    if b in A:
        print(sum(A) - b)
    else:
        print(sum(A) + b)

