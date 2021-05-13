import sys
#import time
#from collections import deque, Counter, defaultdict
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
s = list(rs()+"R")
cnt=0
ans=[0]*(len(s)-1)
for i in range(len(s)-1):
    cnt+=1
    if s[i]=="R" and s[i+1]=="L":
        ans[i]+=cnt-(cnt//2)
        ans[i+1]+=cnt//2
        cnt=0
        hook=i
        continue
    if s[i]=="L" and s[i+1]=="R":
        ans[hook]+=cnt//2
        ans[hook+1]+=cnt-(cnt//2)
        cnt=0
        continue
print(*ans)
