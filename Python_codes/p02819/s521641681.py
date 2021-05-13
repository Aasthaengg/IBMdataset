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

def make_is_prime(N):
    prime = [1 for i in range(N+1)]
    prime[0] = prime[1] = 0
    for i in range(2,N+1):
        if prime[i] == 0: continue
        j = i**2
        while (j <= N):
            prime[j] = 0
            j += i
    return prime

a = make_is_prime(10**5+5)

N = int(input())

for i in range(N,10**5+5):
    if a[i] == 1:
        print(i)
        sys.exit()
