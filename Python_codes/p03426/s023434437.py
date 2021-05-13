def dist(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])
H,W,D = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
G = {}
for i in range(H):
    for j in range(W):
        G[A[i][j]] = (i,j)
C = {}
for j in range(1,D+1):
    k = 1
    C[j] = 0
    while j+k*D<=H*W:
        C[j+k*D] = C[j+(k-1)*D]+dist(G[j+(k-1)*D],G[j+k*D])
        k += 1
Q = int(input())
for _ in range(Q):
    L,R = map(int,input().split())
    print(C[R]-C[L])