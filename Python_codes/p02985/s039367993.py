n,k=map(int,input().split())
ki=[[] for _ in range(n)]
for _ in range(n-1):
  a,b=map(int,input().split())
  a,b=a-1,b-1
  ki[a].append(b)
  ki[b].append(a)
mod=pow(10,9)+7
from collections import deque
seen=[-1]*n
seen[0]=k
todo=deque([0])
while todo:
  t=todo.popleft()
  s=max(k-2,seen[t]-1)
  for li in ki[t]:
    if seen[li]==-1:
      if s<=0:
        print(0)
        exit()
      seen[li]=s
      s-=1
      todo.append(li)
ans=1
for s in seen:
  ans*=s
  ans%=mod
print(ans)
