import sys
input = sys.stdin.readline

N, M, R = [int(x) for x in input().split()]
r = [int(x) - 1 for x in input().split()]
d = [[float("inf")] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
for _ in range(M):
    A, B, C = [int(x) for x in input().split()]
    d[A - 1][B - 1] = C
    d[B - 1][A - 1] = C
def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
d = warshall_floyd(d)

from itertools import permutations
ans = 10 ** 10
route = list(permutations(r))
for i in route:
    cnt = 0
    for j in range(R - 1):
        cnt += d[i[j]][i[j + 1]]
    ans = min(ans, cnt)

print(ans)


