# 
import queue

H,W=map(int,input().split())
c,b=[],0
for i in [0]*H:
    c.append(input())
    b+=c[-1].count('#')
    
vis=[[0]*W for _ in [0]*H]

q=queue.Queue()
q.put((0,0,1))
res=-1
while not q.empty():
    x,y,d=q.get()
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx,ny=x+dx,y+dy
        if (nx,ny)==(W-1,H-1):
            res=H*W-(d+1)-b
        if 0<=nx<=W-1 and 0<=ny<=H-1:
            if not vis[ny][nx] and c[ny][nx]=='.':
                q.put((nx,ny,d+1))
                vis[ny][nx]=1
        if res>-1:
            break
    if res>-1:
        break
print(res)