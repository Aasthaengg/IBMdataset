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
INF =  float("inf")
import bisect
import statistics

N = int(input())
a = list(map(int, input().split()))

for i in range(N):
    a[i] = a[i] - i

def f(k):
    return sum(map(lambda x: abs(x-k), a))

c = statistics.median(a)
print(int(f(c)))


