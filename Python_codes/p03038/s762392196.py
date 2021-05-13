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

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

B = []
for i in range(M):
    B.append(list(map(int, input().split())))

B = sorted(B, key=lambda x: x[1], reverse=True)

j = 0
for b in B:
    for i in range(b[0]):
        if A[j] < b[1]:
            A[j] = b[1]
            j += 1
            if j == N:
                print(sum(A))
                sys.exit()
        else:
            print(sum(A))
            sys.exit()

print(sum(A))