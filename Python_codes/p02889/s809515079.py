INF = 10 ** 14
N, M, L = map(int,input().split())

MAP1 = [[INF for i in range(N)] for j in range(N)]

for _ in range(M):
    A, B, C = map(int,input().split())
    MAP1[A-1][B-1] = C
    MAP1[B-1][A-1] = C

for k in range(N):
    for i in range(N):
        for j in range(N):
            MAP1[i][j] = min(MAP1[i][j], MAP1[i][k] + MAP1[k][j])

MAP2 = [[INF for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        if MAP1[i][j] <= L:
            MAP2[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            MAP2[i][j] = min(MAP2[i][j], MAP2[i][k] + MAP2[k][j])

Q = int(input())

for _ in range(Q):
    s, t = map(int,input().split())
    if MAP2[s-1][t-1] == INF:
        print(-1)
    else:
        print(MAP2[s-1][t-1] - 1)