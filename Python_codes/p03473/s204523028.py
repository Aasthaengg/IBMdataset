import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

m = int(input())
ans = 24 + 24 - m
print(ans)