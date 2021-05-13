ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
ceil = math.ceil

n = ni()
A = lma()
B = lma()
D = [B[i]-A[i] for i in range(n)]
tmp = 0

for d in D:
    if d>0:
        d//=2
    tmp+=d
f=False
if tmp>=0:
    f=True

yn(f)
