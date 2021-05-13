import sys
#import time
#import copy
from collections import deque, Counter, defaultdict
#from fractions import gcd
#import bisect
import heapq
import time

start = time.time()
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))

h,w = rl()
c=[rl() for _ in range(10)]
#g=[[inf]*h for _ in range(h)]



for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j]=min(c[i][j], c[i][k]+c[k][j])

ans=0
for _ in range(h):
    a=rl()
    for num in a:
        if num==-1:
            continue
        ans+=c[num][1]
print(ans)