ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
a,b = ma()
k2 = abs(b-a)
if k2%2==0:
    print(k2//2+min(b,a))
else:
    print("IMPOSSIBLE")
