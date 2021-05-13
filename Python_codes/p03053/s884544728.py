from collections import deque
inf=float("inf")

def BFS():
    color=[["white" for _ in range(w)] for _ in range(h)]
    D=[[inf for _ in range(w)] for _ in range(h)]
    queue=deque([])

    for i in range(h):
        for j in range(w):
            if A[i][j]=="#":
                queue.append([i,j])
                color[i][j]="black"
                D[i][j]=0

    while len(queue)>0:
        x,y=queue.popleft()
        for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
            X,Y=x+i,y+j
            if 0<=X<h and 0<=Y<w:
                if color[X][Y]=="white":
                    color[X][Y]="gray"
                    D[X][Y]=D[x][y]+1
                    queue.append([X,Y])
        color[x][y]="black"

    return D


h,w=map(int,input().split())
A=[list(input()) for _ in range(h)]
D=BFS()
ans=0
for i in range(h):
    ans=max(ans,max(D[i]))
print(ans)