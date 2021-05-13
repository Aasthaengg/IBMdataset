import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections


a,b = map(int,input().split())
if (a+b)%3 == 0:
    print("Possible")
elif a%3 == 0:
    print("Possible")
elif b%3 == 0:
    print("Possible")
else:
    print("Impossible")