from collections import deque
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
XY = [(-1, 0), (1, 0), (0, 1), (0, -1)]
ans = 0

def dfs(h, w):
    Step = [[0]*W for _ in range(H)]
    Step[h][w] = 0
    stack = deque([(h, w)])
    visited =[[False]*W for _ in range(H)]
    while stack:
        i, j = stack.popleft()
        visited[i][j] = True
        for dx, dy in XY:
            x = i + dx
            y = j + dy
            if 0 <= x <= H-1 and 0 <= y <= W-1:
                if x == h and y == w:
                    continue
                if Step[x][y]:
                    continue
                if S[x][y] == '#':
                    continue
                stack.append((x, y))
                Step[x][y] = Step[i][j] + 1
    ans = 0
    for step in Step:
        ans = max(ans, max(step))
    return ans

for h in range(H):
    for w in range(W):
        if S[h][w] != '#':
            ans = max(ans, dfs(h, w))

print(ans)