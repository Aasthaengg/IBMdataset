from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq

n, k = list(map(int, input().split()))
h = [0] + list(map(int, input().split()))

INF = 10**10
dp = [INF]*(n+5)
dp[1] = 0

for i in range(2,n+1):
    temp = [dp[j] + abs(h[i] - h[j]) for j in range(i-1, max(0,i-k-1), -1)]
    dp[i] = min(temp)

print(dp[n])

