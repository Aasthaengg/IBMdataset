from copy import deepcopy
from collections import deque
h,w=map(int,input().split())
ss=[]
u=[(-1,0),(1,0),(0,1),(0,-1)]
ans=0
for i in range(h):
    ss.append(list(input()))
for i in range(h):
    for j in range(w):
        s=deepcopy(ss)
        if s[i][j]=="#":
            continue
        if s[i][j]==".":
            tmp=0
            x,y=i,j
            s[x][y]=0
            que=deque()
            que.append([x,y])
            while que:
                x,y=que.popleft()
                for xx,yy in u:
                    nx,ny=x+xx,y+yy
                    if 0<=nx<h and 0<=ny<w:
                        if s[nx][ny]==".":
                            s[nx][ny]=s[x][y]+1
                            if tmp<s[nx][ny]:
                                tmp=s[nx][ny]
                            que.append([nx,ny])
        if tmp>ans:
            ans=tmp
print(ans)            