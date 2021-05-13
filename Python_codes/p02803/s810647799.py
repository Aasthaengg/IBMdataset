from collections import deque

H, W = map(int, input().split())
mazes = [list(input()) for _ in range(H)]

dis = [[0, 1], [0, -1], [1, 0], [-1, 0]]
answer = 0
for h in range(H):
  for w in range(W):
    if mazes[h][w] == '#':
      continue
    else:
      last = 0
      arrived = [[0 for _ in range(W)] for __ in range(H)]
      routes = deque([[h, w]])
      arrived[h][w] = 1
      while(len(routes) > 0):
        hy, wx = routes.pop()
        move = arrived[hy][wx]
        last = move
        for y, x in dis:
          if 0 <= hy+y < H and 0 <= wx+x < W and mazes[hy+y][wx+x] == '.' and arrived[hy+y][wx+x] == 0:
            routes.appendleft([hy+y, wx+x])
            arrived[hy+y][wx+x] = move + 1
      answer = max(answer, last-1)
print(answer)