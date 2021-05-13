import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from collections import deque

def agc033_a():
    H, W = map(int, readline().split())
    dist = [[-1] * W for _ in range(H)]
    que = deque()
    for i, ln in enumerate(read().split()):
        for j, c in enumerate(ln.strip().decode('UTF-8')):
            if c == '#':
                que.append((i, j))
                dist[i][j] = 0

    while que:
        x, y = que.popleft()
        for i, j in ((x-1, y), (x, y-1), (x, y+1), (x+1, y)):
            if i < 0 or H-1 < i or j < 0 or W-1 < j: continue
            if dist[i][j] != -1: continue
            dist[i][j] = dist[x][y] + 1
            que.append((i, j))

    ans = 0
    for row in dist:
        ans = max(max(row), ans)
    print(ans)

agc033_a()