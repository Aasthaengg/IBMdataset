from collections import deque
H,W=map(int,input().split())
maze=[]
white=0
for i in range(H):
    s=input()
    c=s.count(".")
    white+=c
    maze.append(s)
path=[[None]*W for _ in range(H)]
path[0][0]=1
q=deque([[0,0]])
while q:
    h,w=q.popleft()
    for nh,nw in ([h+1,w],[h-1,w],[h,w+1],[h,w-1]):
        if nh<0 or nh>H-1 or nw<0 or nw>W-1:
            continue
        if maze[nh][nw]=="#" or path[nh][nw]!=None:
            continue
        q.append([nh,nw])
        path[nh][nw]=path[h][w]+1
        if nh==H-1 and nw==W-1:
            print(white-path[nh][nw])
            exit()
print(-1)