N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
  a, b = map(lambda x: int(x)-1, input().split())
  G[a].append(b)

for v in G[0]:
  if N-1 in G[v]:
    print("POSSIBLE")
    exit()
print("IMPOSSIBLE")
