from collections import deque
import sys

sys.setrecursionlimit(10**7)

n=int(input())
to=[[] for _ in range(n)]
eda=[]
for _ in range(n-1):
  a,b=map(int,input().split())
  to[a-1].append(b-1)
  to[b-1].append(a-1)
  eda.append([a-1,b-1])
  
c=list(map(int,input().split()))

c.sort(reverse=True)

cd=deque(c)
poi=[0 for _ in range(n)] 
vi=[-1 for _ in range(n)]

vi[0]+=1
def dfs(now):
  vi[now]+=1
  v=cd.popleft()
  poi[now]+=v
  for i in to[now]:
    if vi[i]==-1:
      dfs(i)
  
dfs(0)

ans=0

for u in eda:
  x,y=u
  ans+=min(poi[x],poi[y])
  
print(ans)
for u in range(n):
  poi[u]=str(poi[u])
  
print(' '.join(poi))
      

