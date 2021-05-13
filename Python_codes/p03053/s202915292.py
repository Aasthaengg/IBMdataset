h,w=map(int,input().split())
G=[input() for _ in range(h)]

from collections import deque
move=[(0,1),(0,-1),(1,0),(-1,0)]

que=deque([])

for i in range(h):
    for j in range(w):
        if G[i][j]=='#':
            que.append((i,j,0))

c=0
visit=[[0]*w for _ in range(h)]
while len(que)>0:
    ni,nj,c=que.popleft()
    for di,dj in move:
        mi,mj=ni+di,nj+dj
        if 0<=mi<h and 0<=mj<w and G[mi][mj]=='.' and visit[mi][mj]==0:
            visit[mi][mj]=1
            que.append((mi,mj,c+1))
print(c)
