n,m,l = map(int,input().split())

A = [[0 for i in range(m)]for j in range(n)]
B = [[0 for i in range(l)]for j in range(m)]
C = [[0 for i in range(l)]for j in range(n)]

for i in range(n):
    lst = list(map(int,input().split()))
    for j in range(m):
        A[i][j] = lst[j]

for i in range(m):
    lst = list(map(int,input().split()))
    for j in range(l):
        B[i][j] = lst[j]
        
for i in range(n):
    for j in range(l):
        total = 0
        for k in range(m):
            total += A[i][k] * B[k][j]
        C[i][j] = total
    s = map(str, C[i])
    print(" ".join(s))
