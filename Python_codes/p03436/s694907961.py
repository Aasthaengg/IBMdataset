from collections import deque,Counter
import itertools
h,w=map(int,input().split())
s=[]
for i in range(h):
    si=list(input())
    s.append(si)
bfs_res=0;
que=deque()
visited=[[-1]*w for i in range(h)]

visited[0][0]=0
que.append((0,0,0))
while que:
    y,x,d=que.popleft()
    for i,j in ([1,0],[-1,0],[0,1],[0,-1]):
        newy,newx=y+i,x+j
        if newy<0 or newx<0 or newy>=h or newx>=w:continue
        if s[newy][newx]=="." and visited[newy][newx]==-1:
            visited[newy][newx]=d+1
            que.append((newy,newx,d+1))
            
s=list(itertools.chain.from_iterable(s))
print(-1 if visited[-1][-1]==-1 else Counter(s)['.']-visited[-1][-1]-1)
