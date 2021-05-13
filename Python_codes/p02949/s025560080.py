import sys
sys.setrecursionlimit((10 ** 6))
input = sys.stdin.readline
N, M, P = map(int, input().split())
INF = float('inf')
G = [[] for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a, b, c = a - 1, b - 1, c - P
    G[a].append((b, -c))
dist = [INF] * N
dist[0] = 0
for i in range(N):
    for e in range(N):
        for w, c in G[e]:
            if dist[e] != INF and dist[w] > dist[e] + c:
                dist[w] = dist[e] + c

ans = -dist[N - 1]
is_negative = [False] * N
for i in range(N):
    for e in range(N):
        for w, c in G[e]:
            if dist[e] != INF and dist[w] > dist[e] + c:
                dist[w] = dist[e] + c
                is_negative[w] = True

            if is_negative[e]:
                is_negative[w] = True

if is_negative[N - 1]:
    print(-1)
else:
    print(max(ans, 0))
