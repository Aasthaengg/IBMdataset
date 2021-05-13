from collections import defaultdict, deque
N = int(input())
G = defaultdict(lambda: [])
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


def bfs(v):
    seen = [0]*(N+1)
    queue = deque()
    dist = [-1]*(N+1)
    dist[v] = 0
    seen[v] = 1
    queue.append(v)
    while queue:
        q = queue.popleft()
        for nx in G[q]:
            if seen[nx]:
                continue
            dist[nx] = dist[q] + 1
            seen[nx] = 1
            queue.append(nx)
        # if not G[q]:
        #     queue.popleft()
        #     continue
        # g = G[q].popleft()
        # if seen[g]:
        #     continue
        # seen[g] = 1
        # dist[g] = dist[q] + 1
        # queue.append(g)
    return dist

d_1 = bfs(1)
d_N = bfs(N)
f = 1
s = 1
for v in range(2, N):
    if d_1[v] <= d_N[v]:
        f += 1
    else:
        s += 1
if f > s:
    print("Fennec")
else:
    print("Snuke")