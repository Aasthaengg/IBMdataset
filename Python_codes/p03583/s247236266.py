ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

N = ni()
mx = 3501
for w in range(1,mx):
    for h in range(1,mx):
        t1=N*w*h
        t2=4*w*h-N*h-N*w
        if t2<=0:continue
        if t1%t2==0:
            print(h,w,t1//t2)
            exit()
