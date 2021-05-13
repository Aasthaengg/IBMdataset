from collections import deque

N = int(input())
Edge = [[]for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)


def bfs(G, root):
    n = len(G)
    Parents = [-1] * n
    Depth = [0] * n
    dq = deque([root])
    dq2 = deque()
    visited = [0] * n
    while dq:
        u = dq.pop()
        for v in G[u]:
            if visited[v]:
                continue
            else:
                dq2 += [v]
                Depth[v] = Depth[u] + 1
                Parents[v] = u
        dq.extend(dq2)
        dq2 = deque()
        visited[u] = 1
    return Depth, Parents


Depth, Parents = bfs(Edge, 0)
cnt = (Depth[-1] - 1)//2
now = N-1
while cnt:
    cnt -= 1
    now = Parents[now]
Edge[Parents[now]].remove(now)

Q = deque()
Q.append(0)
Done = [0] * N
Done[0] = 1
ans = 1
while Q:
    now = Q.popleft()
    for nex in Edge[now]:
        if Done[nex]:
            continue
        else:
            Q.append(nex)
            Done[nex] = 1
            ans += 1

if ans > N // 2:
    print('Fennec')
else:
    print('Snuke')
