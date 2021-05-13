H,W,D = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

plc = {}
for h in range(H):    
    for w in range(W):
        mm = A[h][w]
        plc[mm] = (h,w)

cst = {}
for i in range(1,D+1):
    cst[i] = 0
for i in range(D+1,H*W+1):
    cst[i] = cst[i-D]+abs(plc[i][0]-plc[i-D][0])+abs(plc[i][1]-plc[i-D][1])


Q = int(input())
for i in range(Q):
    L,R = map(int,input().split())
    print(cst[R]-cst[L])




