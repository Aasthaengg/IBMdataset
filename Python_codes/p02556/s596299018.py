import sys
#import time
from collections import deque, Counter, defaultdict
#from fractions import gcd
import bisect
import heapq
#import math
import itertools
import numpy as np
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))

n = ri()
a = []
b = []
for i in range(n):
    x,y = rl()
    a.append(x+y)
    b.append(x-y)
a.sort()
b.sort()
print(max(a[-1]-a[0], b[-1]-b[0]))