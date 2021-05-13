from collections import deque
 
H, W = [int(x) for x in input().split()]
cell = [list(input()) for i in range(H)]
black = 0
stack = deque([[0,0]])
for h in range(H):
    for w in range(W):
        if cell[h][w] == '#':
            black += 1

dp = [[-1]*W for _ in range(H)]
dp[0][0] = 0
while len(stack) > 0:
    y,x = stack.popleft()
    for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < H and 0 <= nx < W and cell[ny][nx] == '.' and dp[ny][nx] == -1:
            dp[ny][nx] = dp[y][x]+1
            stack.append([ny, nx])

if dp[-1][-1] != -1:
    print(H*W-black-dp[-1][-1]-1)
else:
    print(-1)