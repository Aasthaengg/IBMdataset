from collections import deque
# H,Wの向きに注意
H,W=map(int,input().split())
A=[input() for i in range(H)]
ans=0
V=[[0 for i in range(W)] for j in range(H)]

def bfs(q):
    tmp=deque(q)
    ch = [[False for i in range(W)] for j in range(H)]
    count = 0
    d=[[-1,0],[1,0],[0,-1],[0,1]]
    while tmp:
        x,y=tmp.popleft()
        for a,b in d:
            nx=x+a
            ny=y+b
            if 0<=nx<H and 0<=ny<W:
                if ch[nx][ny]!=True and A[nx][ny]==".":
                    V[nx][ny]=V[x][y]+1
                    ch[nx][ny]=True
                    tmp.append([nx,ny])
            else:
                continue
ju=[]
for i in range(H):
    for j in range(W):
        if A[i][j]=="#":
            ju.append([i,j])
bfs(ju)
for i in range(H):
    for j in range(W):
        if not A[i][j]=="#":
             ans=max(ans,V[i][j])
print(ans)

