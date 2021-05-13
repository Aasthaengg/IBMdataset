(n, m, l) = [int(i) for i in input().split()]

A = []
B = []
for _ in range(n):
    A.append([int(i) for i in input().split()])
for _ in range(m):
    B.append([int(i) for i in input().split()])

for i in range(n):
    C = [0 for _ in range(l)]
    for j in range(l):
        for k in range(m):
            C[j] += A[i][k] * B[k][j]
    print(" ".join([str(a) for a in C]))