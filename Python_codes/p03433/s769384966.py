import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

n = int(input())
a = int(input())
n%=500
if n>a:
    print("No")
else:
    print("Yes")