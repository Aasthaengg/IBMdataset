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
if n==1:
    print(1)
    exit()
xy = []
for i in range(n):
    xy.append(tma())
co = collections.Counter()

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        x1,y1 = xy[i]
        x2,y2 = xy[j]
        co[(x2-x1,y2-y1)] +=1

ans = 10**9
for num in co.values():
    ans = min(ans,n-num)
print(ans)
