ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("YES") if fl else print("NO")
import collections
import math
import itertools
import heapq as hq
a1,a2,a3 = ma()
if a1+a2+a3>=22:
    print("bust")
else:
    print("win")
