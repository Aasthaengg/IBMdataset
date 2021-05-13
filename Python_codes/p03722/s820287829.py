import sys
from collections import deque

INF = 10 ** 20
def Bellman_Ford(I):
  N = len(I)
  d = [INF for _ in range(N)] # 各頂点への最小コスト
  d[0] = 0 # 自身への距離は0
  visited = [0 for _ in range(N)]
  for i in range(N-1):
    update = False # 更新有無
    task = deque([(0,0,0)])

    visited[0] = i-1
    while task: 
      a, b, c = task.popleft() 
      if d[b] > d[a] + c:
        d[b] = d[a] + c 
        update = True   
      if visited[b] <= i:
        for x, ct in I[b]:
          task.append((b, x, ct))
        visited[b] += 1
    if not update:
        break
        
  # 負閉路の検知
  visited = [0 for _ in range(N)]
  neg = [0 for _ in range(N)]
  for i in range(N):
    update = False # 更新有無
    task = deque([(0,0,0)])
    visited[0] = i-1
    while task: 
      a, b, c = task.popleft() 
      if d[b] > d[a] + c:
        d[b] = d[a] + c 
        update = True 
        neg[b] = 1
        
      if visited[b] <= i:
        for x, ct in I[b]:
          task.append((b, x, ct))
        visited[b] += 1
        
    if not update:
        break
        
    if neg[N-1] == 1:
      return []
    
  return d

N, M = map(int,input().split()) # N:頂点数, M:辺の数
I = [[] for _ in range(N)]
for _ in range(M):
  a, b, c = map(int,input().split()) # 始点,終点,コスト
  I[a-1].append((b-1,-c))
  #I.append((b,a,c)) 
#print(I)
d = Bellman_Ford(I)
print(-d[N-1] if d else "inf")
