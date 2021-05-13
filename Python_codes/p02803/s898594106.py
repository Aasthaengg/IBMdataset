# https://atcoder.jp/contests/abc151/tasks/abc151_d

from collections import deque

h, w = map(int, input().split())
maze = [list(input()) for i in range(h)]


def bfs(sx, sy):
    count = [[0] * w for i in range(h)]
    check = [[0] * w for i in range(h)]
    check[sx][sy] = 1
    d = deque([[sx, sy]])
    while d:
        x, y = d.popleft()
        for i, j in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            tx, ty = x + i, y + j
            if (
                not (0 <= tx < h)
                or not (0 <= ty < w)
                or maze[tx][ty] == "#"
                or check[tx][ty] == 1
            ):
                continue
            else:
                count[tx][ty] = count[x][y] + 1
                check[tx][ty] = 1
                d.append([tx, ty])

    result = 0
    for k in count:
        for l in k:
            result = max(result, l)
    return result


ans = 0
for i in range(w):
    for j in range(h):
        if maze[j][i] == ".":
            ans = max(ans, bfs(j, i))
print(ans)
