import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import deque

    h, w = map(int, readline().split())
    grid = [["!"] * (w + 2)]
    for _ in range(h):
        s = ["!"] + list(input()) + ["!"]
        grid.append(s)
    grid.append(["!"] * (w + 2))

    ans = 0
    for row in range(1, h + 1):
        for col in range(1, w + 1):
            if grid[row][col] != "!":
                black, white = 0, 0
                que = deque()
                que.append((row, col))
                while que:
                    cr, cc = que.popleft()
                    if grid[cr][cc] == "#":
                        black += 1
                        if grid[cr + 1][cc] == ".":
                            que.append((cr + 1, cc))
                        if grid[cr - 1][cc] == ".":
                            que.append((cr - 1, cc))
                        if grid[cr][cc + 1] == ".":
                            que.append((cr, cc + 1))
                        if grid[cr][cc - 1] == ".":
                            que.append((cr, cc - 1))
                    elif grid[cr][cc] == ".":
                        white += 1
                        if grid[cr + 1][cc] == "#":
                            que.append((cr + 1, cc))
                        if grid[cr - 1][cc] == "#":
                            que.append((cr - 1, cc))
                        if grid[cr][cc + 1] == "#":
                            que.append((cr, cc + 1))
                        if grid[cr][cc - 1] == "#":
                            que.append((cr, cc - 1))
                    grid[cr][cc] = "!"

                ans += white * black
    print(ans)


if __name__ == '__main__':
    main()
