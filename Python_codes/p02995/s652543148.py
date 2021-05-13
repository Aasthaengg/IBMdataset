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

# リストのlcm
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

A, B, C, D = map(int, input().split())

c = B // C - (A-1) // C
d = B // D - (A-1) // D
e = B // lcm_base(C, D) - (A-1) // lcm_base(C, D)

print(B-A+1 - (c+d-e))
