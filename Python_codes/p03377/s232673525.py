import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

a,b,x = map(int,input().split())
ab = a+b
if x>=a and x<=ab:
    print("YES")
else:
    print("NO")