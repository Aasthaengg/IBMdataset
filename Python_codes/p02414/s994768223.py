n,m,l=map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

B = []
for i in range(m):
    B.append(list(map(int, input().split())))

ci = []
for i in range(n):
    cij = []
    for k in range(l):
        s = 0
        for j in range (m):
            s += A[i][j] * B[j][k]
        cij.append(s)
    print(" ".join(map(str,cij)))