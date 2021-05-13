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

KK = 10**5+5

N, K = list(map(int, input().split()))
a = list(map(int, input().split()))

dp = [0 for i in range(KK)]

for i in range(KK):
    for j in a:
        if i-j >= 0 and dp[i-j] == 0: dp[i] = 1

if dp[K] == 1:
    print("First")
else:
    print("Second")