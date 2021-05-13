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

W, H, x, y = map(int, input().split())

if x == W/2.0 and y == H/2.0:
    print(W*H/2.0,1)
else:
    print(W*H/2.0,0)


