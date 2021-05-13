from itertools import permutations


def floyd_warshall(dist):
    v = len(dist)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


N, M, R = map(int, input().split())
r = list(map(lambda x: int(x)-1, input().split()))
dist = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    dist[A][B] = dist[B][A] = C
floyd_warshall(dist)
ans = float('inf')
for perm in permutations(r):
    d = 0
    for i in range(R-1):
        d += dist[perm[i]][perm[i+1]]
    ans = min(ans, d)
print(ans)
