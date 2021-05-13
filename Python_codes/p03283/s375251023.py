N,M,Q = list(map(int,input().split()))

LR = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    Ltmp,Rtmp = list(map(int,input().split()))
    LR[Ltmp][Rtmp] += 1

LRc = [[0]*(N+1) for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        LRc[i][j] = LRc[i-1][j]+LRc[i][j-1]-LRc[i-1][j-1]+LR[i][j]

for i in range(Q):
    p,q = list(map(int,input().split()))
    out = LRc[q][q]-LRc[q][p-1]-LRc[p-1][q]+LRc[p-1][p-1]
    print(out)