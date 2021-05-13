n,m,l = map(int,input().split())

a = [[0 for i in range(m)] for j in range(n)]
b = [[0 for i in range(l)] for j in range(m)]
c = [[0 for i in range(l)] for j in range(n)]

for i in range(n):
    mat_tmp = list(map(int,input().split()))
    for j in range(m):
        a[i][j] = mat_tmp[j]

for i in range(m):
    mat_tmp = list(map(int,input().split()))
    for j in range(l):
        b[i][j] = mat_tmp[j]

for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k]*b[k][j]

for i in range(n):
    print(' '.join(str(x) for x in c[i]))