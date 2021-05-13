import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    start = []
    for h in range(H):
        for w in range(W):
            if S[h][w] != "#":
                start.append([h, w])

    res = 0
    for sh, sw in start:
        maze = [[f_inf] * W for _ in range(H)]
        maze[sh][sw] = 0
        que = deque([[sh, sw]])
        while que:
            h, w = que.popleft()
            for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_h, next_w = h + dh, w + dw
                if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                    continue
                elif S[next_h][next_w] == "#":
                    continue
                else:
                    if maze[next_h][next_w] > maze[h][w] + 1:
                        maze[next_h][next_w] = maze[h][w] + 1
                        que.append([next_h, next_w])
        ma = 0
        for h in range(H):
            for w in range(W):
                if S[h][w] != "#":
                    ma = max(ma, maze[h][w])
        res = max(res, ma)
    print(res)


if __name__ == '__main__':
    resolve()
