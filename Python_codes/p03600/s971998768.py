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

n = ri()
a=[rl() for _ in range(n)]
c=[[0]*n for _ in range(n)]



for k in range(n):
    for i in range(n):
        for j in range(n):
            if k==i or k==j or i==j:
                continue
            if a[i][j]==a[i][k]+a[k][j]:
                c[i][j]+=1
            if a[i][j]>a[i][k]+a[k][j]:
                print(-1)
                sys.exit()
            a[i][j]=min(a[i][j], a[i][k]+a[k][j])
ans=0
for i in range(n):
    for j in range(i+1,n):
        if c[i][j]==0:
            ans+=a[i][j]
print(ans)