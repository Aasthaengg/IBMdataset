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
A = [ni() for i in range(n)]
f=False
for a in A:
    if a%2==1:
        f=True
if f:
    print("first")
else:
    print("second")
