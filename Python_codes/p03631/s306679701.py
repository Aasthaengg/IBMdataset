import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

n = input()
t = ""
for i in range(len(n)-1,-1,-1):
    t+=n[i]
if t == n:
    print("Yes")
else:
    print("No")
