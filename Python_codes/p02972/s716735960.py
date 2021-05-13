import sys
#import time
from collections import deque, Counter, defaultdict
#from fractions import gcd
#import bisect
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
a = rl()

ans=[0]*n

for i in range(n,0, -1):
    sum_=0
    iter_=2
    while i*iter_<=n:
        sum_+=ans[i*iter_-1]
        iter_+=1

    if sum_%2!=a[i-1]:
        ans[i-1]=1

print(sum(ans))
if sum(ans)!=0:
    for i, num in enumerate(ans):
        if num==1:
            print(i+1)