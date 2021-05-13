from collections import deque


def BFS():
    color=[["white" for _ in range(w)] for _ in range(h)]
    queue=deque([])
    ans=0

    for i in range(h):
        for j in range(w):
            if color[i][j]=="white" and S[i][j]=="#":
                queue.append([i,j])
                color[i][j]="gray"
                black,white=0,0

                while len(queue)>0:
                    c,d=queue.popleft()
                    if S[c][d]=="#":black +=1
                    else:white +=1

                    sign="." if S[c][d]=="#" else "#"
                    for a,b in [[1,0],[-1,0],[0,1],[0,-1]]:
                        X,Y=c+a,d+b
                        if 0<=X<h and 0<=Y<w:
                            if S[X][Y]==sign and color[X][Y]=="white":
                                color[X][Y]="gray"
                                queue.append([X,Y])
                    color[c][d]="black"
                ans +=black*white

    return ans


h,w=map(int,input().split())
S=[list(input()) for _ in range(h)]
print(BFS())