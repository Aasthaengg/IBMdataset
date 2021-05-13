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
sys.setrecursionlimit(10**6)


H, N = list(map(int, input().split()))
a = []
for i in range(N):
    a.append(list(map(int, input().split())))


dp = [0 for i in range(H+1)]

for h in range(1, H+1):
    dp[h] = min([dp[max(0, h-a[i][0])] + a[i][1] for i in range(N)])

print(dp[H])



