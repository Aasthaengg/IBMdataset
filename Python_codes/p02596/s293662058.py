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

k = ri()
reses=[]
cnt = 1
tmp = 7
for i in range(k+1):
    res = tmp % k
    if res==0:
        print(cnt)
        sys.exit(0)
    tmp = res * 10 + 7
    cnt += 1
print(-1)