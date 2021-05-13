from collections import  deque
h,w = map(int,input().split())
mp = []
for _ in range(h):
    row = list(input())
    mp.append(row)

q = deque()
dist = [[-1] * w for _ in range(h)]

for col in range(h):
    for row in range(w):
        if mp[col][row] == '#':
            q.append((col,row))
            dist[col][row] = 0
ans = 0
while q:
    now_x,now_y = q.popleft()
    ans = dist[now_x][now_y]
    for x,y in ((1,0), (0,1), (-1,0), (0,-1)):
        next_x = now_x + x
        next_y = now_y + y
        if 0 <= next_x < h and 0 <= next_y < w :
            if dist[next_x][next_y] < 0:
                q.append((next_x, next_y))
                dist[next_x][next_y] = ans + 1

print(ans)
