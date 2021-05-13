n,q=map(int,input().split())
from collections import deque
edge=[[] for _ in range(n)]
ans=[0]*n
for i in range(n-1):
  a,b=map(lambda x:int(x)-1,input().split())
  edge[a].append(b)
  edge[b].append(a)

for i in range(q):
  p,x=map(int,input().split())
  p-=1
  ans[p]+=x

done=[False]*n
q=deque([])
q.append(0)
done[0]=True
while q:
  v=q.popleft()
  done[v]=True
  for c in edge[v]:
    if done[c]==False:
      ans[c]+=ans[v]
      q.append(c)
    
print(*ans) 
  
