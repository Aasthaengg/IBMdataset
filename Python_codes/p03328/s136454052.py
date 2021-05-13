import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop

import collections

a,b = map(int,input().split())
print(int((b-a)*(b-a+1)/2-b))