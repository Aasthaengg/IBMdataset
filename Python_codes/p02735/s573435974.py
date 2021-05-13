import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline

H, W = map(int, readline().split())
s = tuple(map(str, read().split()))
INF = 10 ** 10
grid = [[INF] * W for _ in range(H)]
start = (0, 0)
queue = deque([start])
grid[0][0] = 0
while queue:
    x, y = queue.pop()
    for i, j in ((0, 1), (1, 0)):
        new_x = x + i
        new_y = y + j
        if new_x >= H or new_y >= W:
            continue
        else:
            if s[x][y] == '.' and s[new_x][new_y] == '#':
                cnt = grid[x][y] + 1
                if grid[new_x][new_y] > cnt:
                    grid[new_x][new_y] = cnt
                    queue.append((new_x, new_y))
            else:
                if grid[new_x][new_y] > grid[x][y]:
                    grid[new_x][new_y] = grid[x][y]
                    queue.append((new_x, new_y))

answer = grid[H - 1][W - 1]
if s[0][0] == '#':
    answer += 1
print(answer)
