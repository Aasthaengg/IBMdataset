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
n,m = rl()
a = rl()

li=dict(Counter(a))
for _ in range(m):
    b, c = rl()
    if c in li:
        li[c]+=b
    else:
        li[c]=b
li=sorted(li.items(),key=lambda x: -x[0])
ans=0
res=n
for pair in li:
    if res<=0:
        continue
    if res>=pair[1]:
        ans+=pair[0]*pair[1]
        res-=pair[1]
    else:
        ans+=pair[0]*res
        res=0
print(ans)