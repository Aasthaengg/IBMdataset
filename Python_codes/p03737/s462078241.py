import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9 + 7

s,t,u = input().split()
ans = s[0].upper() + t[0].upper() + u[0].upper()
print(ans)