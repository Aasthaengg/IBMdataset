from collections import deque
import sys


H, W = [int(_) for _ in input().split()]

M = []
w_count = 0
for i in range(H):
    s = input()
    w_count += s.count('.')
    M.append(s)

visited = [[False for _ in range(W)] for _ in range(H)]

q = deque([[0, 0, 1]])
while len(q) != 0:
    p = q.popleft()
    x = p[0]
    y = p[1]
    count = p[2]
    if x == W - 1 and y == H - 1:
        print(w_count - count)
        sys.exit(0)
    cands = []
    if x - 1 >= 0:
        cands.append([x-1, y])
    if x + 1 < W:
        cands.append([x+1, y])
    if y - 1 >= 0:
        cands.append([x, y-1])
    if y + 1 < H:
        cands.append([x, y+1])
    for cx, cy in cands:
        if M[cy][cx] == '.' and not visited[cy][cx]:
            q.append([cx, cy, count+1])
            visited[cy][cx] = True
print(-1)
