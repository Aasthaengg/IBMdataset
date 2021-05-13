import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

s = input()
ans = ""
for i in range(len(s)):
    if i%2 == 0:
        ans += s[i]
print(ans)