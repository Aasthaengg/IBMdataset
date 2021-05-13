ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

n = ni()
H = lma()
cnt=0
tmp=0
prev=H[0]
for h in H:
    if prev>=h:
        tmp+=1
    else:
        cnt=max(cnt,tmp)
        tmp=1
    prev=h
print(max(cnt,tmp)-1)
