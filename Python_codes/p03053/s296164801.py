from collections import deque
H,W = map(int, input().split())
A = [input() for _ in range(H)]

inf = 10**6
d = [[inf]*W for _ in range(H)]
q = deque()
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            q.append((i, j, 0))
            d[i][j] = 0
            
while q:
    temp = q.popleft()
    x = temp[0]
    y = temp[1]
    r = temp[2]
    if x > 0 and d[x-1][y] > r+1:
        d[x-1][y] = r+1
        q.append((x-1, y, r+1))
    if y > 0 and d[x][y-1] > r+1:
        d[x][y-1] = r+1
        q.append((x, y-1, r+1))
    if x < H-1 and d[x+1][y] > r+1:
        d[x+1][y] = r+1
        q.append((x+1, y, r+1))
    if y < W-1 and d[x][y+1] > r+1:
        d[x][y+1] = r+1
        q.append((x, y+1, r+1))

ans = 0
for i in range(H):
    ans = max(ans, max(d[i]))
print(ans)