h,w=map(int,input().split())
lists=[list(input()) for i in range(h)]
visited=[[False for i in range(w)] for j in range(h)]
from collections import deque

ans=0
dif=[(-1,0),(1,0),(0,-1),(0,1)]

def solve(i,j):
    global ans 
    ans=ans
    black=0
    white=0
    if visited[i][j]==False:
        if lists[i][j]=="#":
            black+=1
        else:
            white+=1
        visited[i][j]=True
        
    d=deque()
    e=deque()
    d.append((i,j))
    while d:
        while d:
            p=d.popleft()
            x,y=p
            color=lists[x][y]
            for que in dif:
                dx,dy=que
                if 0<=dx+x<h and 0<=dy+y<w:
                    if visited[dx+x][dy+y]==False and lists[dx+x][dy+y]!=color:
                        visited[dx+x][dy+y]=True
                        e.append((dx+x,dy+y))
                        if color=="#":
                            white+=1
                        else:
                            black+=1
        if e:
            d=e
            e=deque()
    ans+=(white)*(black)
flag=True
while flag:
    sub=False
    for i in range(h):
        for j in range(w):
            if visited[i][j]==False:
                solve(i,j)
                sub=True
    if sub==False:
        flag=False
print(ans)
              
