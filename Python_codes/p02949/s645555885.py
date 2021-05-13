N,M,P = map(int,input().split())

adj = [list() for _ in range(N)]
inv = [list() for _ in range(N)]
edges = []

for _ in range(M):
    a,b,c = map(int,input().split())
    inv[b-1].append(a-1)
    adj[a-1].append(b-1)
    edges.append((a-1,b-1,P-c))

stack = [N-1]
reachable1 = {N-1}
while stack:
    v = stack.pop()
    for u in inv[v]:
        if u not in reachable1:
            stack.append(u)
            reachable1.add(u)

stack = [0]
reachable2 = {0}
while stack:
    v = stack.pop()
    for u in adj[v]:
        if u not in reachable2:
            stack.append(u)
            reachable2.add(u)

reachable = reachable1 & reachable2
edges = [(a,b,w) for a,b,w in edges if a in reachable and b in reachable]

dist = [float('inf')]*N
dist[0] = 0

for i in range(len(reachable)-1):
    for a,b,w in edges:
        dist[b] = min(dist[a]+w, dist[b])

# negative cycle
for a,b,w in edges:
    if dist[b] > dist[a] + w:
        print(-1)
        break
else:
    print(max(0,-dist[-1]))