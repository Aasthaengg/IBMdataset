import itertools

N, M, R = map(int, input().split())
r = map(int, input().split())
A = [[1 << 64]*N for _ in range(N)]
for i in range(N):
    A[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    A[a-1][b-1] = A[b-1][a-1] = c

# Warshall-Floyd
for k in range(N):
    for i in range(N):
        for j in range(N):
            A[i][j] = min(A[i][j], A[i][k] + A[k][j])

res = 1 << 64
for perm in itertools.permutations([x-1 for x in r]):
    cost = 0
    for i in range(R-1):
        cost += A[perm[i]][perm[i+1]]
    if cost < res:
        res = cost

print(res)
