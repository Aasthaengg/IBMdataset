import collections
import sys
import numpy as np
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
MOD = 10**9+7
import itertools
import math
import functools

a = list(map(int,input().split()))
li = []
for i in range(len(a)):
    for j in range(i+1,len(a)):
        cost = abs(a[i]-a[j])
        li.append(cost)
li.sort()
li[-1] = 0
print(sum(li))