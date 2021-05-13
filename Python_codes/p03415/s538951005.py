import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

a = input()
b = input()
c = input()
ans = a[0] + b[1] + c[2]
print(ans)