import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

a = list(map(int,input().split()))
k = int(input())
for i in range(k):
    a.sort()
    a[-1]*=2
print(sum(a))