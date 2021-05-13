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


S = input() + "0"
mod = 2019

dp = [0]
a = 1
for i in range(len(S)-1):
    dp.append((dp[-1] + int(S[len(S)-2-i])*a%mod) % mod)
    a = (a * 10) % mod

count = Counter(dp)

ans = 0
for v in list(count.values()):
    ans += v*(v-1)//2
print(ans)
