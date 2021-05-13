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
x,y,z,k = ma()
A = lma()
B=lma()
C=lma()
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
i,j,m = 0,0,0
h=[(-A[i]-B[j]-C[m],i,j,m)]
cnt=0
d=collections.defaultdict(lambda:True)
while cnt<k:
    ans,i,j,m=hq.heappop(h)
    print(-ans)
    if i+1<x and d[(i+1,j,m)]:
        hq.heappush(h,(-A[i+1]-B[j]-C[m],i+1,j,m))
        d[(i+1,j,m)]=False
    if j+1<y and d[(i,j++1,m)]:
        hq.heappush(h,(-A[i]-B[j+1]-C[m],i,j+1,m))
        d[(i,j+1,m)]=False
    if m+1<z and d[(i,j,m+1)]:
        hq.heappush(h,(-A[i]-B[j]-C[m+1],i,j,m+1))
        d[(i,j,m+1)]=False
    cnt+=1
