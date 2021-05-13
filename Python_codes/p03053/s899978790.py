import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import deque

    h, w = map(int, readline().split())
    que = deque()
    grid = [[] for _ in range(h + 2)]
    grid[0] = ["#"] * (w + 2)
    grid[-1] = ["#"] * (w + 2)

    for row in range(1, h + 1):
        s = input()
        for col, c in enumerate(s, 1):
            if c == "#":
                que.append((row, col, 0))
        grid[row] = ["#"] + list(s) + ["#"]

    cnt = 0

    while que:
        cr, cc, cnt = que.popleft()
        if grid[cr + 1][cc] == ".":
            que.append((cr + 1, cc, cnt + 1))
            grid[cr + 1][cc] = "#"
        if grid[cr - 1][cc] == ".":
            que.append((cr - 1, cc, cnt + 1))
            grid[cr - 1][cc] = "#"
        if grid[cr][cc + 1] == ".":
            que.append((cr, cc + 1, cnt + 1))
            grid[cr][cc + 1] = "#"
        if grid[cr][cc - 1] == ".":
            que.append((cr, cc - 1, cnt + 1))
            grid[cr][cc - 1] = "#"
    print(cnt)


if __name__ == '__main__':
    main()
