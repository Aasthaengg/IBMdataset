from itertools import product
N=int(input())
F = [[[0 for _ in range(3)] for _ in range(6)] for _ in range(N+1)]
for i in range(1,N+1):
    A = list(map(int,input().split()))
    F[i][1][1] = A[0]
    F[i][1][2] = A[1]
    F[i][2][1] = A[2]
    F[i][2][2] = A[3]
    F[i][3][1] = A[4]
    F[i][3][2] = A[5]
    F[i][4][1] = A[6]
    F[i][4][2] = A[7]
    F[i][5][1] = A[8]
    F[i][5][2] = A[9]
P = [[0 for _ in range(11)] for _ in range(N+1)]
for i in range(1,N+1):
    P[i] = list(map(int,input().split()))
pmax = -10**10
for x in product((0,1),repeat=10):
    if sum(x)>0:
        G = [[0 for _ in range(3)] for _ in range(6)]
        G[1][1] = x[0]
        G[1][2] = x[1]
        G[2][1] = x[2]
        G[2][2] = x[3]
        G[3][1] = x[4]
        G[3][2] = x[5]
        G[4][1] = x[6]
        G[4][2] = x[7]
        G[5][1] = x[8]
        G[5][2] = x[9]
        p = 0
        for i in range(1,N+1):
            cnt = 0
            for j in range(1,6):
                for k in range(1,3):
                    if F[i][j][k]==1 and G[j][k]==1:
                        cnt += 1
            p += P[i][cnt]
        pmax = max(pmax,p)
print(pmax)    