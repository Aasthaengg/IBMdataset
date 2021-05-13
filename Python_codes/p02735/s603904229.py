H,W=map(int,input().split())
S=[input()for _ in range(H)]

from collections import deque
maze=[[10**4]*W for _ in range(H)]
maze[0][0]=1*(S[0][0]=='#')
que=deque([[0,0]])
while que:
    y,x=que.popleft()
    for i,j in [(1,0),(0,1)]:
        nexty,nextx=y+i,x+j
        if nexty>=H or nextx>=W:
            continue
        else:
            if S[y][x]=='.':
                if S[nexty][nextx]=='.':
                    if maze[nexty][nextx]>maze[y][x]:
                        maze[nexty][nextx]=maze[y][x]
                        que.append([nexty,nextx])
                else:
                    if maze[nexty][nextx]>maze[y][x]+1:
                        maze[nexty][nextx]=maze[y][x]+1
                        que.append([nexty,nextx])
            elif S[y][x]=='#':
                if maze[nexty][nextx]>maze[y][x]:
                    maze[nexty][nextx]=maze[y][x]
                    que.append([nexty,nextx])

print(maze[H-1][W-1])