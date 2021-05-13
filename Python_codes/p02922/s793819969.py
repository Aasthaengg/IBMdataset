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
cnt=1
ans=0
while cnt<b:
    cnt=cnt-1 +a
    ans+=1
print(ans)
