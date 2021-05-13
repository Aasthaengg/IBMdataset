import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9 + 7

x,y = map(int,input().split())
a = set([1,3,5,7,8,10,12])
b = set([4,6,9,11])
c = set([2])
if (x in a and y in a) or (x in b and y in b) or(x in c and y in c):
    print("Yes")
else:
    print("No")