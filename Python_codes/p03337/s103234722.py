import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

a,b = map(int,input().split())
c = max(a+b,a-b)
c = max(c,a*b)
print(c)