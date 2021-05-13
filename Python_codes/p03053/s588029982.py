#template
def inputlist(): return [int(k) for k in input().split()]
#template
H,W = inputlist()
graph = [0]*H
for i in range(H):
    graph[i] = list(input())
from collections import deque
que = deque()
seen = [[False]*W for _ in range(H)]
li = []
for x in range(H):
    for y in range(W):
        if graph[x][y] == '#':
            tp = (x,y)
            li.append(tp)
que.append(li)
dx = [1,0,-1,0]
dy = [0,1,0,-1]
count = 0
while len(que) != 0:
    l = que.popleft()
    lis = []
    for tup in l:
        xa = tup[0]
        ya = tup[1]
        for i in range(4):
            nx = xa + dx[i]
            ny = ya + dy[i]
            if nx >= H or ny >= W or nx < 0 or ny < 0:
                continue
            if graph[nx][ny] == '#':
                continue
            graph[nx][ny] = '#'
            lis.append((nx,ny))
    count+=1
    if len(lis) == 0:
        print(count-1)
        exit()
    que.append(lis)