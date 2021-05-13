W,H,N=map(int,input().split())

Z=[[0]*W for _ in range(H)]

for _ in range(N):
    X,Y,a=map(int,input().split())

    if a==1:
        for y in range(H):
            for x in range(0,X):
                Z[y][x]=1
    elif a==2:
        for y in range(H):
            for x in range(X,W):
                Z[y][x]=1
    elif a==3:
        for x in range(W):
            for y in range(0,Y):
                Z[y][x]=1
    else:
        for x in range(W):
            for y in range(Y,H):
                Z[y][x]=1

S=0
for l in Z:
    S+=sum(l)
print(H*W-S)
