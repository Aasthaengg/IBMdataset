n, m, l = [int(i) for i in input().split()]

A = []
for i in range(n):
    A.append([int(i) for i in input().split()])

B = []
for i in range(m):
    B.append([int(i) for i in input().split()])

C = [[0] * l for i in range(n)]

for i in range(n):
    for j in range(l):
        C[i][j] = sum(A[i][k] * B[k][j] for k in range(m))

for i in range(n):
    print(*C[i])