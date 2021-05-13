H,W,D = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
C = {i:0 for i in range(1,H*W+1)}
for i in range(H):
    for j in range(W):
        C[A[i][j]] = (i,j)
dist = {i:[] for i in range(1,D+1)}
for i in range(1,D+1):
    dist[i].append(0)
    y0,x0 = C[i]
    for j in range(1,(H*W-i)//D+1):
        y1,x1 = C[i+j*D]
        dist[i].append(dist[i][-1]+abs(y1-y0)+abs(x1-x0))
        y0 = y1
        x0 = x1
Q = int(input())
for _ in range(Q):
    L,R = map(int,input().split())
    i = L%D
    if i==0:
        i = D
    j1 = (L-i)//D
    j2 = (R-i)//D
    print(dist[i][j2]-dist[i][j1])