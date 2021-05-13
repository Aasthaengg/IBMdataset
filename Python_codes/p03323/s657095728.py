import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

a,b = map(int,input().split())
if a>=9  or b>=9:
    print(":(")
else:
    print("Yay!")