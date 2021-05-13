import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    H, W = map(int, readline().split())

    grid = ["." * (W + 2)]

    for _ in range(H):
        s = "." + input() + "."
        grid.append(s)
    grid.append("." * (W + 2))

    res = []
    for row in range(1, H + 1):
        cur = ""
        for col in range(1, W + 1):
            if grid[row][col] == "#":
                cur += "#"
            else:
                cnt = 0
                for r in (row - 1, row, row + 1):
                    for c in (col - 1, col, col + 1):
                        if grid[r][c] == "#":
                            cnt += 1
                cur += str(cnt)
        res.append(cur)

    for x in res:
        print(x)


if __name__ == '__main__':
    main()
