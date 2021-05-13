import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    h, w, a, b = map(int, readline().split())
    grid = [["0"] * w for _ in range(h)]

    for row in range(h):
        for col in range(w):
            c = 0
            if row < b:
                c ^= 1
            if col < a:
                c ^= 1
            grid[row][col] = str(c)

    for i in range(h):
        print("".join(grid[i]))


if __name__ == '__main__':
    main()
