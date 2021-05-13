import sys
input = sys.stdin.readline

def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


N, M, L = map(int, input().split())
INF = 10 ** 10
d = [[INF for _ in range(N)] for _ in range(N)]
D = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
    d[i][i] = 0
for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    d[A][B] = C
    d[B][A] = C
d = warshall_floyd(d)

for i in range(N):
    for j in range(N):
        if 0 < d[i][j] <= L:
            D[i][j] = 1
        elif d[i][j] == 0:
            D[i][j] = 0
D = warshall_floyd(D)

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    print(D[s][t] - 1 if D[s][t] != INF else -1)
