from collections import deque

h, w = map(int,input().split())

cnt = 0
maze = []
for i in range(h):
    t = list(input())
    cnt += t.count('.')
    maze.append(t)
    
dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = deque([(0, 0)])

distance = [[-1]*w for _ in range(h)]
distance[0][0] = 0

while queue:
    y, x = queue.popleft()
    for dxi, dyi in zip(dx, dy):
        if (0<=x+dxi<w and 0<=y+dyi<h) and maze[y+dyi][x+dxi] == "." and distance[y+dyi][x+dxi] == -1:
            distance[y+dyi][x+dxi] = distance[y][x]+1
            queue.append((y+dyi, x+dxi))

if distance[h-1][w-1] != -1:
    print(cnt-(distance[h-1][w-1]+1))
else:
    print(-1)