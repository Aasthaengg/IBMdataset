N, K = map(int, input().split())
mx = (N-1)*(N-2)/2
if mx < K:
  print(-1)
  exit()
pair = []
for i in range(N-1):
  pair += [[i+1, N]]
add = mx - K
edge = []
for i in range(N-1):
  for j in range(i):
    edge += [[i+1, j+1]]

for i in range(int(add)):
  pair += [edge[i]]

print(len(pair))
for i, j in pair:
  print(i, j)