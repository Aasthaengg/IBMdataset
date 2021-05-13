h,w=map(int,input().split())
A=[]
for i in range(h):
    A.append(list(input()))
kabe=0
for i in range(h):
    for j in range(w):
        if A[i][j]=="#":
            kabe+=1
def bfs():
    while queue:
        x,y,d=queue.pop()
        #print("xyd",x,y,d)
        for i in range(4):
            xx=x+dx[i] ; yy=y+dy[i]
            if xx==h-1 and yy==w-1:
                print(h*w-d-2-kabe);exit()
            if 0<=xx<h and 0<=yy<w and A[xx][yy]==".":
                A[xx][yy]="#"
                queue.appendleft([xx,yy,d+1])


from collections import deque
dx=[-1,0,1,0] ;dy=[0,1,0,-1]
queue=deque([[0,0,0]])
bfs()
print(-1)
