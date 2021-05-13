x,y,a,b,c=map(int,input().split())
p=sorted(list(map(lambda x:int(x)*-1,input().split())))
q=sorted(list(map(lambda x:int(x)*-1,input().split())))
r=sorted(list(map(lambda x:int(x)*-1,input().split())))
import heapq
v=p[:x]+q[:y]+r
heapq.heapify(v)
ans=0
for i in range(x+y):
  ans+=heapq.heappop(v)
print(-ans)