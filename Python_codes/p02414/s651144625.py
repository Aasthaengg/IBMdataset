n,m,l = (int(x) for x in input().split())


A = [[int(x) for x in input().split()] for l in range(n)]
B = [[int(x) for x in input().split()] for l in range(m)]

C = [[0]*(l) for i in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k]*B[k][j]

for i in range(n):
    for j in range(l-1):
        print(str(C[i][j])+" ",end = "")
    print(str(C[i][l-1]))

