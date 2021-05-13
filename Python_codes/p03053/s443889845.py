from collections import deque

H, W = map(int, input().split())
que = deque()
A = [[0 for i in range(W)] for j in range(H)]
white_num = 0
for i in range(H):
    S = input()
    for j in range(W):
        if S[j] == '.':
            A[i][j] = -1
            white_num += 1
        elif S[j] == '#':
            A[i][j] = 0
            que.append([j, i])

ans = 0
while len(que) > 0:
    x, y = que.popleft()
    for k in range(4):
        nx = x + [1, 0, -1, 0][k]
        ny = y + [0, 1, 0, -1][k]
        if nx < 0 or ny < 0 or nx >= W or ny >= H:
            continue
        if A[ny][nx] == -1:
            que.append([nx, ny])
            A[ny][nx] = A[y][x] + 1
            ans = max(ans, A[ny][nx])
print(ans)