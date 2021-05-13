import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

n = int(input())
a = int(input())
c = n**2
print(c-a)