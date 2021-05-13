import sys
from collections import deque
H,W=map(int,input().split())
A=[[c for c in l.strip()] for l in sys.stdin]
maze=[[3000]*W for i in range(H)]
q=deque([])
start=[]
dy=[1,0,-1,0]
dx=[0,1,0,-1]
for i in range(H):
  for j in range(W):
    if(A[i][j]=="#"):
      q.append((i,j))
#print(start)
x=0
y=maze[:]

for i in q:
  maze[i[0]][i[1]]=0
while(q):
  c=q.popleft()
  for j in range(4):
    if(c[0]+dy[j]>=0 and c[0]+dy[j]<H and c[1]+dx[j]>=0 and c[1]+dx[j]<W):
      if(maze[c[0]+dy[j]][c[1]+dx[j]]==3000 and A[c[0]+dy[j]][c[1]+dx[j]]=="."):
        q.append((c[0]+dy[j],c[1]+dx[j]))
        maze[c[0]+dy[j]][c[1]+dx[j]]=maze[c[0]][c[1]]+1
        
        x=max(x,maze[c[0]+dy[j]][c[1]+dx[j]])
print(x)
