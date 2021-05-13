import sys
#import time
from collections import deque, Counter, defaultdict
#from fractions import gcd
import bisect
#import heapq
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))
n = ri()
l = rl()

l.sort()
ans=0
for i in range(n):
    for j in range(i):
        ans+=bisect.bisect_left(l, l[i]+l[j])-(i+1)
print(ans)