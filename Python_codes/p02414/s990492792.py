I = input().split()
n = int(I[0])
m = int(I[1])
l = int(I[2])

a = [[0 for i2 in range(m)] for i1 in range(n)]
b = [[0 for i2 in range(l)] for i1 in range(m)]
c = [[0 for i2 in range(l)] for i1 in range(n)]

for i in range(n):
    A = input().split()
    for j in range(m):
        a[i][j] = int(A[j])

for i in range(m):
    B = input().split()
    for j in range(l):
        b[i][j] = int(B[j])

for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k] * b[k][j]
        print(str(c[i][j]), end = '')
        if j != l - 1:
            print(' ', end = '')
    print()