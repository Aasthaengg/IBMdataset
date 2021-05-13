n, m, l=map(int, input().split(" "))

A = [ [ int(a) for a in input().split() ] for i in range(n) ]
B = [ [ int(b) for b in input().split() ] for i in range(m) ]
C = [ [ 0 for i in range(l) ] for i in range(n) ]

for i in range(n):
    for j in range(l):
        for jj in range(m):
                 C[i][j] = C[i][j] + A[i][jj] * B[jj][j]

    print(" ".join([str(_) for _ in C[i]]))