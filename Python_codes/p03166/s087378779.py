from collections import deque

def read_pair():
    return map(int, input().strip().split())

# Read graph
N, M = read_pair()
adj = [[] for x in range(N)]
rev = [[] for y in range(N)]

outdegree = [0] * N
for i in range(M):
    x, y = read_pair()

    # Use 0-indexed labels
    x -= 1
    y -= 1

    adj[x].append(y)
    rev[y].append(x)
    outdegree[x] += 1

maxpath = [0] * N
q = deque()

for x in range(N):
    if outdegree[x] == 0:
        q.append(x)

while q:
    x = q.popleft()
    for y in adj[x]:
        maxpath[x] = max(maxpath[x], 1 + maxpath[y])
    for z in rev[x]:
        outdegree[z] -= 1
        if outdegree[z] == 0:
            q.append(z)

print(max(maxpath))
