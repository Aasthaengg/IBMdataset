ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("YES") if fl else print("NO")
import collections
import math
import itertools
import heapq as hq
n = ni()
P = lma()
cnt = 0
for i in range(n):
    if P[i] != i+1:
        cnt+=1
f = False
if cnt==2 or cnt==0:
    f=True
yn(f)
