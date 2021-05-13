n, m, l = map(int, raw_input().split())

A = [[0] for i in range(n)]
B = [[0] for i in range(m)]
temp = 0

for i in range(n):
    A[i] = map(int, raw_input().split())
for i in range(m):
    B[i] = map(int, raw_input().split())

C = [[0 for i in range(l)] for j in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            temp += A[i][k] * B[k][j]
        C[i][j] = temp
        temp = 0
for i in range(n):
    print " ".join(map(str, C[i]))