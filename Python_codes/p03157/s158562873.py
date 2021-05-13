import sys
from collections import deque

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


def bfs_grid(H, W, grid):

    d = [[False for _ in range(W)] for _ in range(H)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans = 0

    for sy in range(H):
        for sx in range(W):
            if d[sy][sx]:
                continue

            q = deque()
            q.append((sx, sy))
            d[sy][sx] = True
            black = 0
            white = 0
            while q:
                x, y = q.popleft()
                now_color = grid[y][x]
                if now_color:
                    white += 1
                else:
                    black += 1
                for m in move:
                    nx, ny = x + m[0], y + m[1]
                    if 0 <= nx < W and 0 <= ny < H:
                        if not d[ny][nx] and grid[ny][nx] != now_color:
                            d[ny][nx] = True
                            q.append((nx, ny))

            ans += black * white

    return ans


def main():
    H, W = in_nn()
    grid = in_map2(H)

    print(bfs_grid(H, W, grid))


if __name__ == '__main__':
    main()
