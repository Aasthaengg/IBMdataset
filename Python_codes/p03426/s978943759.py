H,W,D=map(int, input().split())

pos=[0]*(H*W)
for h in range(H):
    a=list(map(int, input().split()))
    for w in range(W):
        pos[a[w]-1]=(h,w)

for i in range(D):
    nowx,nowy=pos[i]
    idx=i
    rui=0
    pos[i]=rui
    while idx+D<H*W:
        idx+=D
        x,y=pos[idx]
        rui=rui+abs(x-nowx)+ abs(y-nowy)
        pos[idx]=rui
        nowx=x
        nowy=y

Q=int(input())
for i in range(Q):
    L,R=map(int, input().split())
    print(pos[R-1]-pos[L-1])
#print(pos)
