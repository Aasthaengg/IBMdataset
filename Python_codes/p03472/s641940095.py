from heapq import *
n,h=map(int,input().split())
k=[]
for _ in [0]*n:
  a,b=map(int,input().split())
  heappush(k,(-a,1))
  heappush(k,(-b,0))
ans=0
while h>0:
  a,i=heappop(k)
  a=-a
  if i:
    ans+=(h+a-1)//a
    break
  else:
    ans+=1
    h-=a
print(ans)