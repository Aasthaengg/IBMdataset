n,m = map(int,input().split())
matrix =[[0 for i in range(m+1)] for j in range(n+1)]

for i in range(n):
    a = list(map(int,input().split()))
    for j in range(m):
        matrix[i][j] = a[j]
        matrix[i][m] += a[j]
        matrix[n][j] += a[j]
        matrix[n][m] += a[j]

for i in range(0,n+1):
    print(' '.join(str(x) for x in matrix[i]))

