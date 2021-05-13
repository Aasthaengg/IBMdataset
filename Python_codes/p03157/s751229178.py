import sys
from sys import stdin
sys.setrecursionlimit(10**7)
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
H, W = [int(_) for _ in stdin.readline().rstrip().split()]
field = [list(stdin.readline().rstrip()) for _ in range(H)]
seen = [[False for i in range(400)] for j in range(400)]
num_b, num_w = 0, 0
ans = 0

def dfs(h, w):
    seen[h][w] = True
    if field[h][w] == '#':
        global num_b
        num_b += 1
    else:
        global num_w
        num_w += 1

    for direction in range(4):
        nh = h + dx[direction]
        nw = w + dy[direction]

        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if field[nh][nw] == field[h][w]:
            continue
        if seen[nh][nw]:
            continue

        dfs(nh, nw)

for i in range(H):
    for j in range(W):
        if field[i][j] == '.':
            continue
        if seen[i][j]:
            continue
        num_b, num_w = 0, 0
        dfs(i, j)
        ans += num_b * num_w 

print(ans)