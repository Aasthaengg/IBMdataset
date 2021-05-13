import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

x,y = map(int,input().split())
cnt = 0
while True:
    a = x*2**cnt
    if a>y:
        break
    cnt+=1
print(cnt)