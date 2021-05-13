import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

n = int(input())
if n>=1000:
    print("ABD")
else:
    print("ABC")