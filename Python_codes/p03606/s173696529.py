import collections
import sys
import numpy as np
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
MOD = 10**9+7
import itertools
import math
import functools

n = int(input())
cnt = 0
for i in range(n):
    l,r = map(int,input().split())
    a = r-l + 1
    cnt += a
print(cnt)