INF = float('inf')

def dijkstra(s,N,M,cost,ans):
  d = [INF] * N
  used = [False] * N
  d[s] = 0
  prvv = [[] for _ in range(N)]
  while True:
    v = -1
    for i in range(N):
      if (not used[i]) and (v == -1): v = i
      elif (not used[i] and d[i] < d[v]): v = i
    if v == -1: break
    used[v] = True
  
    for j in range(N):
      if d[j] > d[v]+cost[v][j]:
        d[j] = d[v]+cost[v][j]
        prvv[j] = [v]
      elif d[j] == d[v]+cost[v][j]:
        d[j] = d[v]+cost[v][j]
        prvv[j].append(v)
  
  for i, vs in enumerate(prvv):
    for v in vs:
      ans.add(tuple(sorted([v,i])))

  return prvv

N,M = map(int,input().split())

cost = [[INF for _ in range(N)] for _ in range(N)]
for i in range(M):
  a,b,c = map(int,input().split())
  cost[a-1][b-1] = c
  cost[b-1][a-1] = c


ans =set([])
for i in range(N):
  dijkstra(i,N,M,cost,ans)
print(M-len(ans))
#print(ans)