H, W = [int(x) for x in input().split()]
G = []
for _ in range(H):
    G.append(input())

import queue, itertools
dist = {(i, j) : -1 for i, j in itertools.product(range(W), range(H))}
dist[(0, 0)] = 1
q = queue.Queue()
q.put((0, 0))

dx = [1,  0, -1,  0]
dy = [0,  1,  0, -1]

while not q.empty():
    x, y = q.get()
    d = dist[(x, y)]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if min(nx, ny) >= 0 and nx <= W - 1 and ny <= H - 1:
            if dist[(nx, ny)] == -1 and G[ny][nx] == '.':
                dist[(nx, ny)] = d + 1
                q.put((nx, ny))
            else: 
                continue

if dist[(W - 1, H - 1)] == -1:
    print(-1)
else:    
    print(H * W - ''.join(G).count('#') - dist[(W - 1, H - 1)])