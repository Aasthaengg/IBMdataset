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

A, B, K = map(int, input().split())

if K<=A:
    print(A-K, B)
elif B-(K-A) >= 0:
    print(0, B-(K-A))
else:
    print(0,0)