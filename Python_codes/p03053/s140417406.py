from collections import deque
inf=10**9


def BFS():
    point=0
    color=[["white" for _ in range(w)] for _ in range(h)]
    D=[[inf for _ in range(w)] for _ in range(h)]

    queue=deque([])
    for i in range(h):
        for j in range(w):
            if A[i][j]=="#":
                queue.append([i,j])
                D[i][j]=0

    while len(queue)>0:
        x,y=queue.popleft()
        for a,b in [[1,0],[-1,0],[0,1],[0,-1]]:
            X,Y=x+a,y+b
            if 0<=X<h and 0<=Y<w:
                if color[X][Y]!="black" and D[X][Y]>D[x][y]+1:
                    color[X][Y]="gray"
                    D[X][Y]=D[x][y]+1
                    point=max(point,D[X][Y])
                    queue.append([X,Y])
        color[x][y]="black"

    return point


h,w=map(int,input().split())
A=[list(input()) for _ in range(h)]
print(BFS())