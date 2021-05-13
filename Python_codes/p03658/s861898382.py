import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

n,k = map(int,input().split())
l = list(map(int,input().split()))
l.sort(reverse= True)
ans = 0
for i in range(k):
    ans += l[i]
print(ans)
