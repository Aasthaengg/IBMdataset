import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

s = list(input())
if s[3] == "7":
    s[3] = "8"
ans = ""
for i in range(len(s)):
    ans += s[i]
print(ans)