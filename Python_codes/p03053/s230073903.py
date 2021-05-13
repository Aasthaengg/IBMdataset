from collections import deque
h, w = map(int, input().split())
a = [[] for _ in range(h)]
for i in range(h):
    a[i] = list(input())

dis = [[1000000 for _ in range(w)] for _ in range(h)]
queue = deque([])

for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            dis[i][j] = 0
            queue.append([i, j])

while queue:
    now = deque.popleft(queue)
    if now[0] != 0:
        if dis[now[0]-1][now[1]] == 1000000:
            dis[now[0]-1][now[1]] = dis[now[0]][now[1]]+1
            queue.append([now[0]-1, now[1]])
            
    if now[0] != h-1:
        if dis[now[0]+1][now[1]] == 1000000:
            dis[now[0]+1][now[1]] = dis[now[0]][now[1]]+1
            queue.append([now[0]+1, now[1]])
            
    if now[1] != 0:
        if dis[now[0]][now[1]-1] == 1000000:
            dis[now[0]][now[1]-1] = dis[now[0]][now[1]]+1
            queue.append([now[0], now[1]-1])
            
    if now[1] != w-1:
        if dis[now[0]][now[1]+1] == 1000000:
            dis[now[0]][now[1]+1] = dis[now[0]][now[1]]+1
            queue.append([now[0], now[1]+1])

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, dis[i][j])

print(ans)