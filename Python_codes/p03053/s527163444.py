from collections import deque

h,w=list(map(int,input().split()))
a=[[c for c in input()] for _ in range(h)]
visit=[[0]*w for _ in range(h)]
q=deque()

for i in range(h):
    for j in range(w):
        if a[i][j]=='#':
            deque.appendleft(q,(i,j,0))
            visit[i][j]=1
ans=0
while len(q)>0:
    i,j,cnt=deque.pop(q)

    ans=max(ans,cnt)

    for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
        ni=i+di
        nj=j+dj
        if 0<=ni<h and 0<=nj<w and visit[ni][nj]==0:
            visit[ni][nj]=1
            deque.appendleft(q,(ni,nj,cnt+1))

print(ans)