from collections import deque

H, W = map(int, input().split())
H += 2
W += 2
grid = '#' * W
for _ in range(H-2):
    grid += '#' + input() + '#'
grid += '#' * W

def bfs(start):
    INF = 10 ** 9
    dist = [INF] * (H*W)
    dist[start] = 0
    q = deque([start])
    move_list = [-1, 1, W, -W]
    while q:
        v = q.popleft()
        dv = dist[v]
        for move in move_list:
            w = v + move
            if grid[w] == '#':
                continue
            dw = dv + 1
            if dw >= dist[w]:
                continue
            dist[w] = dw
            q.append(w)
    return dist[-(W+2)]

d = bfs(W+1)
T = grid.count("#")

if d == 10 ** 9:
  print("-1")
else:
  print(H*W - T - (d+1))