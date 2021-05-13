import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9 + 7

n,m = map(int,input().split())
scc = min(n,m//2)
n -= scc
m -= scc*2

print(scc + m//4)