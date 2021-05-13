from collections import deque


H,W = map(int, input().split())
A = [[str(i) for i in list(input())] for _ in range(H)]

q = deque()
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            q.append((i,j))


ans = 0
dyx = [(1,0), (0,1), (-1,0), (0,-1)]
while q:
    flag = False
    for _ in range(len(q)):
        y,x = q.popleft()
        for dy, dx in dyx:
            ny, nx = y+dy, x+dx
            if not 0 <= ny <= H-1 or not 0 <= nx <= W-1:
                continue
            if A[ny][nx] == ".":
                q.append((ny, nx))
                A[ny][nx] = "#"
                flag = True
    if flag:
        ans += 1

print(ans)


