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

a, b, x = map(int, input().split())

if x <= a**2*b/2.0:
    print(math.atan(a*b**2/(2.0*x))*180/math.pi)
else:
    z = a**2*b - x
    print(math.atan((2.0*z)/(a**3))*180/math.pi)

