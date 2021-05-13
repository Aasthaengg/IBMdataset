import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

a = int(input())
b = int(input())
c = int(input())
d = int(input())
ac = a + c
ad = a + d
bc = b + c
bd = b + d
ans = min(ac,ad)
ans = min(ans,bc)
ans = min(ans,bd)
print(ans)
