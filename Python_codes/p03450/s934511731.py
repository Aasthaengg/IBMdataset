from collections import deque
def check():
  N, M = map(int, input().split())
  edge = [[] for _ in range(N)]
  for i in range(M):
    a,b,d = map(int, input().split())
    edge[a-1].append([b-1,d])
    edge[b-1].append([a-1,-d])
  
  visited = [float('inf')]*N
  D = deque()
  for i in range(N):
    if visited[i]==float('inf'):
      visited[i]=0
      D.append(i)
      while len(D)>0:
        v = D.popleft()
        for w,d in edge[v]:
          if visited[w]==float('inf'):
            visited[w] = visited[v]+d
            D.append(w)
          elif visited[w]!=visited[v]+d:
            return 'No'
  return 'Yes'
print(check())