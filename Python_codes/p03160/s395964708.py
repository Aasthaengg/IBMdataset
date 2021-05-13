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

n = int(input())
h = [0] + list(map(int, input().split()))+[0]

INF = 10**15

dp = [INF]*(n+5)
dp[0] = 0
dp[1] = 0

for i in range(1,n):
    a = dp[i] + abs(h[i+1]-h[i])
    dp[i+1] = min(dp[i+1], a)
    a = dp[i] + abs(h[i + 2] - h[i])
    dp[i+2] = min(dp[i+2], a)

print(dp[n])
