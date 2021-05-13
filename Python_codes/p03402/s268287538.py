import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b = map(int, readline().split())
    grid = []
    for _ in range(50):
        grid.append(["#"] * 100)

    for _ in range(50):
        grid.append(["."] * 100)

    w_row, w_col = 0, 0
    b_row, b_col = 51, 0

    for white in range(a - 1):
        grid[w_row][w_col] = "."
        w_row += 2
        if w_row == 50:
            w_row = 0
            w_col += 2

    for black in range(b - 1):
        grid[b_row][b_col] = "#"
        b_row += 2
        if b_row == 101:
            b_row = 51
            b_col += 2

    print(100, 100)
    for row_state in grid:
        print("".join(row_state))


if __name__ == '__main__':
    main()
