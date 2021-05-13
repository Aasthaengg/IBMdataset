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

# 約数全列挙
def divisors(n):
    i = 1
    ans = []
    while i*i <= n:
        if n % i == 0:
            ans.append(i)
            if i*i != n: ans.append(n // i)
        i += 1
    ans.sort()
    return ans

a = divisors(N)
m = len(a)

if m % 2 == 1:
    print(2*a[m//2] - 2)
else:
    print(a[m//2-1] + a[m//2] - 2)