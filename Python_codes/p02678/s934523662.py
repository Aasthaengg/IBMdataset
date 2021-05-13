from collections import deque
def bfs(N,start,dp):
  visited=[0]*N
  visited[start]=1
  que=deque([start])
  while que:
    a=que.popleft()
    for i in dp[a]:
      if not visited[i]:
        visited[i]=a+1
        que.append(i)
  return visited
N,M=map(int,input().split())
dp=[[] for i in range(N)]
for _ in range(M):
  A,B=map(int,input().split())
  dp[A-1].append(B-1)
  dp[B-1].append(A-1)
visited=bfs(N,0,dp)[1:]
if all(visited):
  print('Yes')
  for i in visited:
    print(i)
else:
  print('No')