import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9+7

n = int(input())
k = int(input())
x = int(input())
y = int(input())
ans = min(n,k)*(x)
n -= k
if n>0:
    ans += n*y
print(ans)