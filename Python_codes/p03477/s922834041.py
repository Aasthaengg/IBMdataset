import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

a,b,c,d= map(int,input().split())
e = a + b
f= c + d
if e > f:
    print("Left")
elif e == f:
    print("Balanced")
else:
    print("Right")