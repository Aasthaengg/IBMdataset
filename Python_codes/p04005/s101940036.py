import collections
import sys
import numpy as np
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
MOD = 10**9+7
import itertools
import math

a,b,c = map(int,input().split())
max_block = a*b*c
max_edge = max(a,b,c)
min_edge = min(a,b,c)
middle_edge = (a+b+c) - max_edge - min_edge
choku1 = (max_edge//2)*min_edge*middle_edge
choku2 = (max_edge//2+1) * min_edge * middle_edge
if max_edge%2 == 0:
    print("0")
else:
    print(abs(choku1-choku2))