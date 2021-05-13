from collections import deque
h,w=map(int,input().split())

maze=[[i for i in input()] for _ in range(h)]

que=deque([[0,0]])

visited=[[0 for _ in range(w)] for _ in range(h)]
visited[0][0]=1

while que:
    n=que.popleft()
    x,y=n[0],n[1]

    if n==(h-1,w-1):
        break

    for i, j in [(1,0), (0,1)]:
        if (x+i >=w) or (y+j >=h) or maze[y+j][x+i] == '#':
            continue
        if visited[y+j][x+i] == 0:
            que.append([x+i,y+j])
        visited[y+j][x+i] += visited[y][x]

print(visited[h-1][w-1]%(10**9+7))
