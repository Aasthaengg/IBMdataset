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

x = []
for i in range(N):
    x.append(list(map(int, input().split())))

p = [i for i in range(N)]
pp = list(itertools.permutations(p))

ans = 0
for ppp in pp:
    for i in range(1,N):
        ans += math.sqrt((x[ppp[i-1]][0]-x[ppp[i]][0])**2 + (x[ppp[i-1]][1]-x[ppp[i]][1])**2)

print(ans / math.factorial(N))