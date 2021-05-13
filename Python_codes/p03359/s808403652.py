import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

a,b = map(int,input().split())
ans = a - 1
for i in range(b+1):
    if a == i:
        ans +=1
print(ans)