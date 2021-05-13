n,m,l = map(int,input().split())
matrix1 =[[0 for i in range(m)] for j in range(n)]
matrix2 =[[0 for i in range(l)] for j in range(m)]
matrix  =[[0 for i in range(l)] for j in range(n)]
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(m):
        matrix1[i][j] = a[j]
for i in range(m):
    a = list(map(int,input().split()))
    for j in range(l):
        matrix2[i][j] = a[j]
for i in range(n):
    for j in range(m):
        for k in range(l):
            matrix[i][k] += matrix1[i][j] * matrix2[j][k]
for i in range(0,n):
    print(' '.join(str(x) for x in matrix[i]))
