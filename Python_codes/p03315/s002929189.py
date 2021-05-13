import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

s = input()
ans = 0
for i in range(len(s)):
    if s[i] == "+":
        ans+=1
    else:
        ans-=1
print(ans)