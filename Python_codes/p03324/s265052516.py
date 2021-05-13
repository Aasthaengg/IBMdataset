import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

d,n = map(int,input().split())
if n != 100:
    print(n*100**d)
else:
    print(101*100**d)