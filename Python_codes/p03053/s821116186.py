from collections import deque


def BFS():
    color=[["white" for _ in range(w)] for _ in range(h)]
    D=[[0 for _ in range(w)] for _ in range(h)]

    num=0
    queue=deque([])
    for i in range(h):
        for j in range(w):
            if A[i][j]=="#":
                queue.append([i,j])
                color[i][j]="gray"

    while len(queue)>0:
        a,b=queue.popleft()
        for c,d in [[1,0],[-1,0],[0,1],[0,-1]]:
            X,Y=a+c,b+d
            if 0<=X<h and 0<=Y<w:
                if color[X][Y]=="white":
                    D[X][Y]=D[a][b]+1
                    num=max(num,D[X][Y])
                    color[X][Y]="gray"
                    queue.append([X,Y])
        color[a][b]="black"

    return num


h,w=map(int,input().split())
A=[list(input()) for _ in range(h)]
print(BFS())