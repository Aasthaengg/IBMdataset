from heapq import heappush,heappop
n,m=map(int,input().split())
d=[]
for i in range(n):
  a,b=map(int,input().split())
  heappush(d,(a,b))
ans=0
while d:
  a,b=heappop(d)
  if m>b:
    ans+=a*b
    m-=b
  else:
    ans+=a*m
    break
print(ans)