n, m, l = map(int, input().split())
A = [[0] * m for _ in range(n)]
B = [[0] * l for _ in range(m)]
C = [[0] * l for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        A[i][j] = a[j]
for i in range(m):
    b = list(map(int, input().split()))
    for j in range(l):
        B[i][j] = b[j]
for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]
for i in range(n):
    for j in range(l - 1):
        print(C[i][j], end=' ')
    print(C[i][l - 1])

