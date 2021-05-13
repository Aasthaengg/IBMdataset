import sys
from collections import deque

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

def bfs(x, y, c):
    global data
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que = deque()
    que.append(((x, y), c))
    data[y][x] = 'visited'
    black = 1
    white = 0

    while que:
        p, color = que.popleft()
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            next_color = '#' if color == '.' else '.'            
            if 0 <= ny and ny <= H-1 and 0 <= nx and nx <= W-1 and \
                    data[ny][nx] == next_color:
                data[ny][nx] = 'visited'
                if next_color == '.':
                    white += 1
                elif next_color == '#':
                    black += 1
                que.append(((nx, ny), next_color))
    return white * black

H, W = rl()
data = [list(rs()) for _ in range(H)]
answer = 0

for y in range(H):
    for x in range(W):
        if data[y][x] == '#':
            answer += bfs(x, y, data[y][x])

print(answer)
# rest
