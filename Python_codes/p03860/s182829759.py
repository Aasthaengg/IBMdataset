import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9+7

s = input().split()
print(s[0][0] + s[1][0] + s[2][0])