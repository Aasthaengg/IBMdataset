import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import deque, defaultdict

    h, w = map(int, readline().split())
    que = deque()
    grid = [["#"] * (w + 2)]

    for row in range(1, h + 1):
        s = input()
        for col, c in enumerate(s, 1):
            if c == "#":
                que.append((row, col, 0))
        grid.append(["#"] + list(s) + ["#"])

    grid.append(["#"] * (w + 2))
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    cnt = 0

    while que:
        cr, cc, cnt = que.popleft()
        for mr, mc in direction:
            nr, nc = cr + mr, cc + mc
            if grid[nr][nc] == ".":
                que.append((nr, nc, cnt + 1))
                grid[nr][nc] = "#"

    print(cnt)


if __name__ == '__main__':
    main()
