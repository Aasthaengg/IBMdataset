import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9 + 7
x = int(input())
cnt = 0
if x<=6:
    print(1)
elif x<=11:
    print(2)
else:
    if x%11 == 0:
        print((x//11)*2)
    elif x%11 > 6:
        print(((x//11)+1)*2)
    else:
        print((x//11)*2 + 1)