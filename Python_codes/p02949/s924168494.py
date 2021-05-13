N, M, P = map(int, input().split())

abc = []
for i in range(M):
  a, b, c = map(int, input().split())
  abc.append([a-1, b-1, c-P])


dist = [-float('inf')]*N
dist[0] = 0
for i in range(N):
  for a, b, c in abc:
    dist[b] = max(dist[b], dist[a] + c)


for a, b, c in abc:
  d = dist[a] + c
  if dist[b] < d:
    dist[b] = float('inf')

for i in range(N-1):
  for a, b, c in abc:
    dist[b] = max(dist[b], dist[a] + c)

if dist[-1] < float('inf'):
  ans = max(0, dist[-1])
else:
  ans = -1

print(ans)