n,m = [int(i) for i in input().split()]

A = [[int(i) for i in input().split()] for j in range(n)]
B = [int(input()) for i in range(m)]

for i in range(n):
    c = 0
    for j in range(m):
        c += A[i][j]*B[j]
    print(c)
