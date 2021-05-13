def warshall_floyd(G):
    import copy
    ret = copy.deepcopy(G)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                ret[i][j] = min(ret[i][j], ret[i][k] + ret[k][j])
    return ret


INF = 10 ** 10
N, M, L = map(int, input().split())

G = [[INF] * N for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    G[A - 1][B - 1], G[B - 1][A - 1] = C, C

MinG = warshall_floyd(G)
GL = [[1 if MinG[i][j] <= L else INF for j in range(N)] for i in range(N)]
MinGL = warshall_floyd(GL)

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    print(-1 if MinGL[s - 1][t - 1] == INF else MinGL[s - 1][t - 1] - 1)
