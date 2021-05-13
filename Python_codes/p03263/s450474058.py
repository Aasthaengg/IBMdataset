H,W=list(map(int,input().split()))
A=[list(map(lambda x: int(x)%2,input().split())) for _ in range(H)]
visit=[[0]*W for _ in range(H)]

pt=[0,0]
disp=False
ans=[]
while True:
    y,x=pt
    visit[y][x]=1
    if A[y][x]==1:
        disp=not disp
    flag=True
    for dy,dx in [[1,0],[0,1],[-1,0],[0,-1]]:
        ny=y+dy
        nx=x+dx
        if 0<=ny<H and 0<=nx<W and visit[ny][nx]==0:
            npt=[ny,nx]
            flag=False
    if flag:
        break

    if disp:
        ans.append('{} {} {} {}'.format(y+1,x+1,npt[0]+1,npt[1]+1))
    
    pt=npt

print(len(ans))
for s in ans:
    print(s)