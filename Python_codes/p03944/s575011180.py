W,H,N=map(int,input().split())
sq=[[1 for i in range(W)] for j in range(H)]

for i in range(N):
    x,y,a=map(int,input().split())
    if a==1:
        for X in range(0,x):
            for Y in range(H):
                sq[Y][X]=0
    if a==2:
        for X in range(x,W):
            for Y in range(H):
                sq[Y][X]=0
    if a==3:
        for X in range(W):
            for Y in range(0,y):
                sq[Y][X]=0
    if a==4:
        for X in range(W):
            for Y in range(y,H):
                sq[Y][X]=0

ans=0
for k in range(H):
    ans+=sum(sq[k])
print(ans)
