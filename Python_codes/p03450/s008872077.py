import heapq
N, M = map(int, input().split())
E = [[] for _ in range(N)]
RE = [[] for _ in range(N)]
S = [0] * N
for _ in range(M):
  l, r, d = map(int, input().split())
  S[l - 1] = 1
  E[l - 1].append([d, r - 1])
  RE[r - 1].append([d, l - 1])
D = [None] * N
def dijkstra(i):
  D[i] = 0
  Q = [[0, i]]
  while Q:
    d, s = heapq.heappop(Q)
    for dist, adj in E[s]:
      if D[adj] == None:
        D[adj] = D[s] + dist
        heapq.heappush(Q, [D[adj], adj])
      elif D[adj] == 'Error' or D[adj] != D[s] + dist:
        D[s] = 'Error'
        break
    else:
      for dist, adj in RE[s]:
        if D[adj] == None:
          D[adj] = D[s] - dist
          heapq.heappush(Q, [D[adj], adj])
        elif D[adj] == 'Error' or D[adj] != D[s] - dist:
          D[s] = 'Error'
          break
      else:
        continue
    break
for i in range(N):
  if D[i] == 'Error':
    print('No')
    break
  elif D[i] == None:
    dijkstra(i)
else:
  for d in D:
    if d == 'Error':
      print('No')
      break
  else:
    print('Yes')