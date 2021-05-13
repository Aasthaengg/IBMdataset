N, M = map(int, input().split())
E = []
for _ in range(M):
  a, b, c = map(int, input().split())
  E.append((a-1, b-1, -c))

INF = 10**20
V = [INF]*N
V[0] = 0
for _ in range(N):
  for a, b, c in E:
    d = V[a]+c
    if d < V[b]: V[b] = d

R = [False]*N
R[-1] = True
for _ in range(N):
  for a, b, c in E:
    R[a] |= R[b]

for a, b, c in E:
  if V[a]+c<V[b] and R[b]:
    print('inf')
    exit()
    
print(-V[-1])