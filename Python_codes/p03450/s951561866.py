import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    L, R, D = map(int, input().split())
    L -= 1
    R -= 1
    G[L].append((R, D))
    G[R].append((L, -D))

visited = [False] * N
dist = [float('inf')] * N
for i in range(N):
    if not visited[i]:
        dist[i] = 0
        stack = [i]
        while stack:
            v = stack.pop()
            visited[v] = True
            for u, d in G[v]:
                if dist[u] == float('inf'):
                    dist[u] = dist[v] + d
                elif dist[u] != dist[v] + d:
                    print('No')
                    exit()
                if not visited[u]:
                    stack.append(u)
print('Yes')
