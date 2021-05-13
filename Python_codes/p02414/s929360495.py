n, m, l = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(n)]
B = [tuple(map(int, input().split())) for _ in range(m)]
C = [[0] * l for _ in range(n)]
for i in range(n):
    for k in range(m):
        for j in range(l):
            C[i][j] += A[i][k] * B[k][j]
for i in range(n):
    print(*C[i])
