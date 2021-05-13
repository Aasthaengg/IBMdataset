import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

a,b,c = map(int,input().split())
if a == b:
    print(c)
elif a == c:
    print(b)
else:
    print(a)