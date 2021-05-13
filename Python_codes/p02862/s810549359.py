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

X, Y = map(int, input().split())

if (X + Y) % 3 != 0:
    print(0)
    sys.exit()

N = (X + Y) // 3
M = X - N

if X < N or Y < N:
    print(0)
    sys.exit()

# C,Pを求める前処理
m = 10**6
mod = 10**9 + 7


fact = [0]*(m+5)
fact_inv = [0]*(m+5)
inv = [0]*(m+5)

fact[0] = fact[1] = 1
fact_inv[0] = fact_inv[1] = 1
inv[1] = 1

for i in range(2,m+5):
    fact[i] = fact[i-1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    fact_inv[i] = fact_inv[i-1] * inv[i] % mod

# nCkをmod（素数）で割った余りを求める．ただしn<10**7
# 前処理はm=n+5まで
def cmb(n,k,mod):
    return fact[n] * (fact_inv[k] * fact_inv[n-k] % mod) % mod

print(cmb(N,M,mod))

