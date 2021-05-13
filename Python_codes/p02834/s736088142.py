from collections import deque


def bfs(s):
    d = [-1] * n
    p = [-1] * n
    dq = deque([s])
    d[s] = 0

    while dq:
        u = dq.popleft()
        for v in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                p[v] = u
                dq.append(v)

    return d, p


n, takahashi, aoki = map(int, input().split())
takahashi -= 1
aoki -= 1
ab = [list(map(int, input().split())) for _ in range(n - 1)]

adj = [[] for _ in range(n)]
for a, b in ab:
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

depth, par = bfs(takahashi)
aoki_move = depth[aoki] // 2 + 1
root = aoki
for _ in range(aoki_move):
    child = root
    root = par[root]

adj[child].remove(root)
adj[root].remove(child)

depth2, par2 = bfs(root)

aoki_move += max(depth2) - 1
print(aoki_move)
