import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9 + 7

a,b,c = map(int,input().split())
if b - a == c -b:
    print("YES")
else:
    print("NO")