import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

x = int(input())
a = int(input())
b = int(input())
x-= a
x%=b
print(x)