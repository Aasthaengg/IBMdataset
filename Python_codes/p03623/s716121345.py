import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

x,a,b = map(int,input().split())
c = abs(x-a)
d = abs(x-b)
if c<d:
    print("A")
else:
    print("B")