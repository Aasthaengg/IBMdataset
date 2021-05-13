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

N, K = list(map(int, input().split()))

# nが小さいとき（<5000）にcmb % modを計算．modは素数でなくてもよい
# 前処理
l = 2500
Com = [[0]*(l+5) for i in range(l+5)]
Com[0][0] = 1
for i in range(1,l+5):
    Com[i][0] = 1
    for j in range(1,i+1):
        Com[i][j] = (Com[i-1][j-1] + Com[i-1][j]) % mod

for i in range(1,K+1):
    print((Com[K-1][i-1] * (Com[N-K][i-1] + Com[N-K][i]) ) % mod)