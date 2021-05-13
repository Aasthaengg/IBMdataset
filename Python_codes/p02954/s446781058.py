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

S = input()

j = 0
flag = 0
ans = [0 for i in range(len(S))]
for i in range(len(S)):
    if S[i] == "L" and flag == 0:
        ans[i-1] += (i -j + 1) // 2
        ans[i] += (i-j) // 2
        j = i
        flag = 1
    if S[i] == "R" and flag == 1:
        ans[j-1] += (i-j) // 2
        ans[j] += (i-j+1) // 2
        j = i
        flag = 0
ans[j-1] += (len(S)-j) // 2
ans[j] += (len(S)-j+1) // 2

ans = map(str, ans)
print(" ".join(ans))