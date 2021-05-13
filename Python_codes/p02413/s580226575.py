n, m = map(int, input().split())
mat = [[0 for x in range(m+1)] for y in range(n+1)]

for i in range(n):
    r = list(map(int,input().split()))
    for j in range(m):
        mat[i][j] = r[j]

for i in range(n):
    for j in range(m):
        mat[i][-1] += mat[i][j]
        mat[-1][j] += mat[i][j]
    mat[-1][-1] += mat[i][-1]

for i in range(n+1):
    print(*mat[i])


