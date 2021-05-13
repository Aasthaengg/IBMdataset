from heapq import heappop,heappush
n,h=map(int,input().split())
a=[]
for i in range(n):
  x,y=map(int,input().split())
  heappush(a,(-x,1))
  heappush(a,(-y,0))
ans=0
while h>0:
  x,y=heappop(a)
  if y:
    ans+=(h-x-1)//(-x)
    break
  else:
    h+=x
    ans+=1
print(ans)