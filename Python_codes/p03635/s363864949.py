import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections


n,m = map(int,input().split())
print((n-1)*(m-1))