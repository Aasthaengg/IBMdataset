from collections import deque

def dfs(tree, cost, root):
    q = deque([root])
    dist = [-1]*N

    dist[root] = cost[root]

    while q:
        v = q.pop()
        for n_v in tree[v]:
            if dist[n_v] < 0:
                dist[n_v] = dist[v] + cost[n_v]
                q.append(n_v)

    return dist

N, Q = map(int, input().split())
tree = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

pts = [0]*N

for _ in range(Q):
    p, x = map(int, input().split())
    pts[p - 1] += x

dist = dfs(tree, pts, 0)

for i in range(N):
    print(dist[i])