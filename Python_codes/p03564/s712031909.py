import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

n = int(input())
k = int(input())
p = 1
for i in range(n):
    p = min(2*p,p+k)
print(p)