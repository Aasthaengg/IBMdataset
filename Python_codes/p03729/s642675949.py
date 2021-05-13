import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9 + 7

a,b,c = input().split()
if a[-1] == b[0] and b[-1] == c[0]:
    print("YES")
else:
    print("NO")