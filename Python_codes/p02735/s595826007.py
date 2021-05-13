from collections import deque
# import math


def bfs(maze, mazeColor, h, w, sy, sx, gy, gx):
    for y in range(h):
        for x in range(w):
            maze[y][x] = float("inf")

    if mazeColor[sy][sx] == '.':
        maze[sy][sx] = 0
    else:
        maze[sy][sx] = 1
    que = deque([[sy, sx]])
    while que:
        y, x = que.popleft()
        for i, j in [(1, 0), (0, 1)]:
            nexty, nextx = y + i, x + j
            distColor = mazeColor[nexty][nextx]
            beforeColor = mazeColor[y][x]
            dist = maze[nexty][nextx]
            if distColor != '#':
                if dist > maze[y][x]:
                    maze[nexty][nextx] = maze[y][x] + 0
                    que.append([nexty, nextx])
            else:
                if dist > maze[y][x]:
                    if beforeColor == '.':
                        maze[nexty][nextx] = maze[y][x] + 1
                    else:
                        maze[nexty][nextx] = maze[y][x] + 0
                    que.append([nexty, nextx])

    # for i in range(len(maze[0])):
    #    print(maze[i])
    print(maze[gy][gx])


h, w = map(int, input().split())
mazeColor = ['#'+'#'*w+'#']
for i in range(h):
    mazeColor.append('#'+input()+'#')
mazeColor.append('#'+'#'*w+'#')

maze = [[0 for j in range(w+2)] for i in range(h+2)]

bfs(maze, mazeColor, h+1, w+1, 1, 1, h, w)
