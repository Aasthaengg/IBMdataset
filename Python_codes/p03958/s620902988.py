import sys
input = sys.stdin.readline
from heapq import heappush,heapify,heappop
k,t=map(int,input().split())
a=list(map(int,input().split()))
b=[]
heapify(b)
ans=[-1]*k
for i in range(t):
    heappush(b,[-a[i],i])
x=heappop(b)
ans[0]=x[1]
x[0]+=1
if x[0]<0:
    heappush(b,x)
for i in range(1,k):
    x=heappop(b)
    if ans[i-1]==x[1] and b:
        y=heappop(b)
        ans[i]=y[1]
        y[0]+=1
        if y[0]<0:
            heappush(b,y)
        heappush(b,x)
    else:
        ans[i]=x[1]
        x[0]+=1
        if x[0]<0:
            heappush(b,x)
cnt=0
for i in range(1,k):
    if ans[i]==ans[i-1]:
        cnt+=1
print(cnt)