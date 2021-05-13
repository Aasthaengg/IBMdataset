import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9+7
MAX = 10**18
MIN = -10**18

n,k = map(int,input().split())
a = list(map(int,input().split()))
print(math.ceil((n-1)/(k-1)))