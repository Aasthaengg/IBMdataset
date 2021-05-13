from collections import deque

N,M=map(int,input().split())
startx=0
starty=0
goalx=M-1
goaly=N-1

S = [["" for j in range(M)] for i in range(N)]#2行3列の場合
#iがyｊがx

point=0

for i in range(N):
    tmp=input()
    for j in range(M):
        S[i][j]=tmp[j]
        if S[i][j]==".":
            point+=1
        
        
seen=[[-1 for j in range(M)] for i in range(N)]
#S = [[0 for j in range(3)] for i in range(2)]　2行3列の場合

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(y,x):

    todox=deque()
    todoy=deque()
    seen[y][x]=1
    todox.append(x)
    todoy.append(y)
    
    while len(todox) !=0:
        x=todox.popleft()
        y=todoy.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<M and ny>=0 and ny<N :
                if nx==goalx and ny==goaly:
                    seen[ny][nx]=seen[y][x]+1
                    #print(seen)
                    return seen[ny][nx]
                        
                if S[ny][nx]==".":
                    
                    
                    
                    if seen[ny][nx] ==-1:
                        #print("mohu",nx,ny)
                        seen[ny][nx] =seen[y][x]+1
                        todox.append(nx)
                        todoy.append(ny)
                
    return -1

ret=dfs(starty,startx)
if ret==-1:
    print(-1)
else:
    print(point-ret)
