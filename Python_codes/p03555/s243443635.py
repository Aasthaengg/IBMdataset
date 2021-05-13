import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

s = input()
t = input()
t2 = t[::-1]
if s == t2:
    print("YES")
else:
    print("NO")
 