n,m,l = (int(x) for x in input().split())
A = [input().split() for i in range(n)]
B = [input().split() for i in range(m)]

C = [[0] * l for i in range(n)]

for i in range(n):
    x = 0
    for j in range(l):
        for k in range(m):
            C[i][j] += int(A[i][k]) * int(B[k][j])
    print(*C[i])
