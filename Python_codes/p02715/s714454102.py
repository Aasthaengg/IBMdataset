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
mod = 10**9+7

N, K  = list(map(int, input().split()))
ans = [0 for i in range(K+1)]

for i in range(K,0,-1):
    a = pow((K // i), N, mod)
    for j in range(2,K+1):
        if i*j <= K:
            a = (a - ans[i*j]) % mod
        else:
            break
    ans[i] = a % mod

# print(ans)

b = [i*ans[i] % mod for i in range(K+1)]
print(sum(b) % mod)



