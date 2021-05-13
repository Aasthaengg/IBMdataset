from collections import deque
N = int(input())
G = dict([(i,[]) for i in range(1,N+1)])
for i in range(N-1):
  a,b,c = map(int,input().split())
  G[a].append([c,b])
  G[b].append([c,a])
Q,K = map(int,input().split())
q = []
for i in range(Q):
  q.append(list(map(int,input().split())))

d = [0 for i in range(N+1)]
deq = deque([K])
seen = [False for i in range(N+1)]
while len(deq) > 0:
  v = deq.popleft()
  for i in G[v]:
    if seen[i[1]] == False:
      d[i[1]] = d[v] + i[0]
      deq.append(i[1])
      seen[i[1]] = True

for i in range(Q):
  [x,y] = q[i]
  print(d[x]+d[y])