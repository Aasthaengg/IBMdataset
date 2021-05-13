#create date: 2020-07-03 14:46

import sys
stdin = sys.stdin
from collections import deque

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    h, w = na()
    g = [[1] * (w+2)]
    white = 0
    for i in range(h):
        r = ns()
        white += r.count(".")
        g.append([1] + [1 if s=="#" else 0 for s in r] + [1])
    g.append([1] * (w+2))
    q = deque([[1,1]])
    move = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if g[nx][ny] > 0:
                continue
            g[nx][ny] = g[x][y] + 1
            q.append((nx, ny))
    if g[h][w] == 0:
        print(-1)
    else:
        print(white - g[h][w] - 1)



if __name__ == "__main__":
    main()