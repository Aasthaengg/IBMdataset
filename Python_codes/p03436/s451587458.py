h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
black=0
for i in range(h):
    black+=s[i].count("#")




from collections import deque
que=deque()
que.append([0,0])
s[0][0]="#"
count=[[0]*w for _ in range(h)]
while que:
    
    x=que.pop()
    dx_dy=[[0,1],[1,0],[0,-1],[-1,0]]
    for k in range(4):
        nx=x[0]+dx_dy[k][0]
        ny=x[1]+dx_dy[k][1]
        if 0<=nx<=h-1 and 0<=ny<=w-1 and s[nx][ny]==".":
            s[nx][ny]="#"
            count[nx][ny]=count[x[0]][x[1]]+1
            que.appendleft([nx,ny])
if s[-1][-1]=="#":
    print(h*w-count[-1][-1]-black-1)
else:
    print(-1)
