import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

n = input()
for i in range(len(n)-2):
    if n[i] == n[i+1] and n[i+1] == n[i+2]:
        print("Yes")
        sys.exit()
print("No")