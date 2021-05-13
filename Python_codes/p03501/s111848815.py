import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

n,a,b = map(int,input().split())
ans = min(a*n,b)
print(ans)