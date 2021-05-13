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

## a, bを無向辺として，隣接リストを作成
n, m = list(map(int, input().split()))
a = ["" for i in range(n)]

N = 10**9 + 7

for i in range(n):
    a[i] = str(input())

dp = [[0]*m for i in range(n)]

flag = 0
for i in range(n):
    if a[i][0] == "#" or flag == 1:
        dp[i][0] = 0
        flag = 1
    else:
        dp[i][0] = 1

flag = 0
for j in range(m):
    if a[0][j] == "#" or flag == 1:
        dp[0][j] = 0
        flag = 1
    else:
        dp[0][j] = 1

for i in range(1,n):
    for j in range(1,m):
        if a[i][j] == "#":
            dp[i][j] = 0
        else:
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % N

print(dp[n-1][m-1] % N)
