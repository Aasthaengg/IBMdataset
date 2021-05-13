import sys

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

mod = 10**9 + 7


def main():

    H, W = in_nn()
    grid = in_map2(H)

    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1

    for y in range(H):
        for x in range(W):
            if x + 1 < W and grid[y][x + 1]:
                dp[y][x + 1] += dp[y][x]
                dp[y][x + 1] %= mod
            if y + 1 < H and grid[y + 1][x]:
                dp[y + 1][x] += dp[y][x]
                dp[y + 1][x] %= mod

    print(dp[H - 1][W - 1])


if __name__ == '__main__':
    main()
