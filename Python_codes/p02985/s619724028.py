from collections import deque

n,k=map(int,input().split())
visited=[False]*n
visited[0]=True
color=[0]*n
color[0]=k
mod=10**9+7

graph=[[] for i in range(n)]

for i in range(n-1):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


Q=deque()
Q.append((0))
ans=k

while Q:
  p=Q.popleft()
  cnt=0
  for i in graph[p]:
    if visited[i]==False:
        cnt+=1
        Q.append((i))
        visited[i]=True

  if p==0:
      for i in range(cnt):
          ans*=k-i-1
          ans%=mod

  else:
      for i in range(cnt):
          ans*=k-i-2
          ans%=mod


print(ans%mod)