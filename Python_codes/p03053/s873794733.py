import sys
from collections import deque
from copy import copy

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def bfs_grid(H, W, s, grid):

    q = deque(s)
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans = 0

    while True:

        nq = deque()
        f = False
        while q:
            now = q.popleft()
            x, y = now
            for m in move:
                nx, ny = x + m[0], y + m[1]
                if 0 <= nx < W and 0 <= ny < H:
                    if grid[ny][nx]:
                        f = True
                        grid[ny][nx] = False
                        nq.append((nx, ny))

        if f:
            ans += 1
        if nq:
            q = nq
        else:
            break

    return ans


def main():

    H, W = in_nn()
    grid = in_map2(H)

    s = []
    for y in range(H):
        for x in range(W):
            if not grid[y][x]:
                s.append((x, y))

    if len(s) == H * W:
        print(0)
        exit()

    print(bfs_grid(H, W, s, grid))


if __name__ == '__main__':
    main()
