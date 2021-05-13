H,W=map(int,input().split())
S=[input() for i in range(H)]
visit=[[False]*W for i in range(H)]
par=[[None]*W for i in range(H)]
dd={}
X=[-1,0,1,0]
Y=[0,-1,0,1]
for j in range(H):
    for i in range(W):
        if visit[j][i]:
            continue
        if S[j][i]=='.':
            continue
        lH=[]
        lH.append((j,i,0))#0が黒
        par[j][i]=(i,j)
        num=0
        while lH:
            y,x,t=lH.pop()
            visit[y][x]=True
            for k in range(4):
                nx=x+X[k]
                ny=y+Y[k]
                if 0<=nx<W and 0<=ny<H:
                    if visit[ny][nx]:
                        continue
                    if t==0 and S[ny][nx]=='.':
                        visit[ny][nx]=True
                        num+=1
                        lH.append((ny,nx,1))
                    elif t==1 and S[ny][nx]=='#':
                        visit[ny][nx] = True
                        par[ny][nx]=(i,j)
                        lH.append((ny,nx,0))
        dd[(i,j)]=num
ans=0
for j in range(H):
    for i in range(W):
        if S[j][i]=='#':
            x,y=par[j][i]
            ans+=dd[(x,y)]
print(ans)
