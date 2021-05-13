import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

a,b,c,d = map(int,input().split())
ab = abs(b - a)
bc = abs(c - b)
ac = abs(c - a)
if ac <= d:
    print("Yes")
    sys.exit()
if ab <= d and bc <= d:
    print("Yes")
    sys.exit()
print("No")