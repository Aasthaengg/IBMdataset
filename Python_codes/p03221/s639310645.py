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
n, m = rl()
lis=[[] for _ in range(n+1)]
shi=[tuple(rl()) for _ in range(m)]
ans=dict()

for i in shi:
    lis[i[0]].append(i[1])

for i, com in enumerate(lis):
    if len(com)==0:continue

    for j,num in enumerate(sorted(com)):
        ans[num]="0"*(6-len(str(i)))+ str(i) + "0"*(6-len(str(j+1)))+str(j+1)

for i in shi:
    print(ans[i[1]])