import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

s = input()
cnt = 0
for i in range(len(s)):
    if s[i] == "o":
        cnt+=1
if cnt == 0:
    print(700)
else:
    print(700+ 100*cnt)