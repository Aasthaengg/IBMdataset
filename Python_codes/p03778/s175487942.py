import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

w,a,b = map(int,input().split())
l = max(a,b)
s = min(a,b)
print(max(l-s-w,0))