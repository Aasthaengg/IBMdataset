N, K = (int(i) for i in input().split())

graph = [[] for i in range(N)]
for i in range(N-1):
    a, b = (int(i) for i in input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

from collections import deque
def BFS(N, K, graph, start):
    c = [-1 for i in range(N)]
    Q = deque([])
    Q.append(start)
    c[start] = K
    while Q:
        v = Q.popleft()
        if v == start:
            lc = K - 1
        else:
            lc = K - 2
        for u in graph[v]:
            if c[u] == -1:
                if lc == 0:
                    print(0)
                    exit()
                c[u] = lc
                lc -= 1
                Q.append(u)
    return c

c = BFS(N, K, graph, 0)

MOD = 10**9+7
ans = 1
for i in c:
    ans *= i
    ans %= MOD
print(ans)