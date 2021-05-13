import itertools
N, M, R = map(int, input().split())
r = list(map(int, input().split()))
r = [x - 1 for x in r]
d = [[float("inf")] * N for i in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c


def warshall_floyd(d):
    # d[i][j]: iからjへの最短距離
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

warshall_floyd(d)
# print(d)
ans = float('inf')
for x in itertools.permutations(r):
    cost = 0
    # print(x)
    for i in range(len(x) - 1):
        # print(i)
        cost += d[x[i]][x[i+1]]
    ans = min(ans, cost)
print(ans)