import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

a,b,c = map(int,input().split())
ab = a + b
ac = a + c
bc = b + c
ans = min(ab,ac)
ans = min(ans,bc)
print(ans)