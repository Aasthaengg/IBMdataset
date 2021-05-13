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
a, b, c = list(map(int, input().split()))

dp = [[-1]*3 for i in range(n+1)]
dp[1][0] = a
dp[1][1] = b
dp[1][2] = c

for i in range(2,n+1):
    a, b, c = list(map(int, input().split()))
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + a
    dp[i][1] = max(dp[i - 1][2], dp[i - 1][0]) + b
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + c

print(max([dp[n][0], dp[n][1], dp[n][2]]))
