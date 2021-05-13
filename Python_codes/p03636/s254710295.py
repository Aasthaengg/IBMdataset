import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections


s = input()
n = len(s)-2
ans = s[0] + str(n) + s[-1]
print(ans)