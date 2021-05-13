n,m,q = map(int, input().split())

A = [[0 for i in range(n+1)] for j in range(n+1)]
Acum = [[0 for i in range(n+1)] for j in range(n+1)]

for _ in range(m):
    L,R = map(int,input().split())
    A[L-1][R-1] += 1

#2次元累積和
for i in range(n):
    for j in range(n):
        Acum[i+1][j+1] = Acum[i][j+1] + Acum[i+1][j] - Acum[i][j] + A[i][j]

# print(Acum)
for _ in range(q):
    p,q= map(int,input().split())
    A = Acum[q][q]-Acum[p-1][q]-Acum[q][p-1]+Acum[p-1][p-1]
    print(A)


