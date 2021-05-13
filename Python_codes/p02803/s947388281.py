import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from collections import deque

H,W = map(int,readline().split())
H += 2; W += 2
grid = '#' * W
for _ in range(H-2):
    grid += '#' + readline().rstrip().decode() + '#'
grid += '#' * W

def bfs(start):
    INF = 10 ** 9
    dist = [INF] * (H*W)
    dist[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        dv = dist[v]
        for move in (-1,1,W,-W):
            w = v + move
            if grid[w] == '#':
                continue
            dw = dv + 1
            if dw >= dist[w]:
                continue
            dist[w] = dw
            q.append(w)
    return max(x for x in dist if x < INF)

answer = max(bfs(v) for v in range(H*W) if grid[v] != '#')
print(answer)
