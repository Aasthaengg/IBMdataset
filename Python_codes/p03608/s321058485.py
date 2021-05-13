import itertools


def warshall_floyd(G):
    import copy
    ret = copy.deepcopy(G)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                ret[i][j] = min(ret[i][j], ret[i][k] + ret[k][j])
    return ret


N, M, R = map(int, input().split())
r = list(map(int, input().split()))
G = [[10 ** 10] * N for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A - 1][B - 1] = C
    G[B - 1][A - 1] = C
W, ans = warshall_floyd(G), 10 ** 10
for p in itertools.permutations(r, R):
    ans = min(ans, sum([W[p[i] - 1][p[i + 1] - 1] for i in range(R - 1)]))
print(ans)
