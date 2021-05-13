from collections import deque

h, w = map(int, input().split())
tizu = [list(input()) for _ in range(h)]
check = [[False for _ in range(w)] for _ in range(h)]
ans = 0

queue = deque()
for i in range(h):
    for j in range(w):
        if tizu[i][j] == "#":
            queue.append([i, j])
            queue.append(0)
            check[i][j] = True

direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]        
while queue:
    pos = queue.popleft()
    cnt = queue.popleft()
    for dy, dx in direct:
        n_y = pos[0] + dy
        n_x = pos[1] + dx
        if n_y == -1 or n_y == h or n_x == -1 or n_x == w:
            continue
        if check[n_y][n_x]:
            continue
        check[n_y][n_x] = True
        ans = max(ans, cnt + 1)
        queue.append([n_y, n_x])
        queue.append(cnt + 1)
print(ans)