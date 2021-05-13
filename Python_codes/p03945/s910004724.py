import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9+7

s = input()
cnt = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt+=1
print(cnt)