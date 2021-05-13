from collections import deque, Counter
n, x, y = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(n-1):
    G[i].append(i+1)
    G[i+1].append(i)
G[x-1].append(y-1)
G[y-1].append(x-1)
c = Counter()
for i in range(n):
    q = deque([i])
    dist = [-1]*n
    dist[i] = 0
    while q:
        cur = q.popleft()
        for nx in G[cur]:
            if dist[nx] != -1:
                continue
            dist[nx] = dist[cur]+1
            q.append(nx)
    for j, d in enumerate(dist):
        if i == j:
            continue
        c[d] += 1
for i in range(1, n):
    print(c[i]//2)
