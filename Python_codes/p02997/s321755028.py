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

N, K = map(int, input().split())

if N < 0 or K > (N-1)*(N-2)//2:
    print(-1)
else:
    M = (N-1)*(N-2)//2 - K
    print(M+N-1)
    for i in range(1,N):
        print(i,N)
    count = 0
    for i in range(1,N):
        for j in range(i+1,N):
            if count == M:
                sys.exit()
            print(i,j)
            count += 1
