import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

a,b = input().split()
if a == "H" and b == "H":
    print("H")
elif a == "D" and b == "D":
    print("H")
else:
    print("D")