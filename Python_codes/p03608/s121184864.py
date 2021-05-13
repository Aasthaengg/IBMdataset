from itertools import permutations
N, M, R = map(int, input().split())
r = [int(i)-1 for i in input().split()]
inf = float("inf")
mat = [[inf]*N for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    if mat[a-1][b-1] > c:
        mat[a-1][b-1] = mat[b-1][a-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])


ans = inf
for p in list(permutations(r)):
    dist = 0
    for i in range(1, len(p)):
        dist += mat[p[i]][p[i-1]]
    ans = min(ans, dist)

print(ans)
