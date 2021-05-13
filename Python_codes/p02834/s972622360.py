from collections import deque
N, u, v = map(int, input().split())
u, v = u-1, v-1
AB = [list(map(int, input().split())) for a in range(N-1)]

G = [[] for a in range(N)]

for ab in AB:
  G[ab[0]-1].append(ab[1]-1)
  G[ab[1]-1].append(ab[0]-1)

qA = deque([v])
qT = deque([u])
costsA = [0 for a in range(N)]
doneA = [0 for a in range(N)]
costsT = [0 for a in range(N)]
doneT = [0 for a in range(N)]

doneA[v] = 1
doneT[u] = 1

def bfs(q, costs, done):
  while q:
    start = q.popleft()
    for i in G[start]:
      if done[i] == 0:
        q.append(i)
        costs[i] = costs[start] + 1
        done[i] = 1

bfs(qA, costsA, doneA)
bfs(qT, costsT, doneT)

distances = [0]
for i in range(N):
  if costsA[i] > costsT[i]:
    distances.append(costsA[i])

print(max(distances)-1)
