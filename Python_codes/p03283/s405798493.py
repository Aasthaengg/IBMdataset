n, m, q = map(int, input().split())
mat = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    l, r = map(int, input().split())
    mat[l][r] += 1

for i in range(n+1):
    for j in range(n+1):
        mat[i][j] += mat[i-1][j]
        mat[i][j] += mat[i][j-1]
        mat[i][j] -= mat[i-1][j-1]
ans = 0
for _ in range(q):
    l, r = map(int, input().split())
    print(mat[r][r]-mat[r][l-1]-mat[l-1][r]+mat[l-1][l-1])
