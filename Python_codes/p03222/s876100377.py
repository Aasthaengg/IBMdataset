import sys
import itertools

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


mod = 10 ** 9 + 7


def main():

    H, W, K = in_nn()

    if W == 1:
        print(1)
        exit()

    comb_t = itertools.product(range(2), repeat=W - 1)
    comb = [[0 for _ in range(3)] for _ in range(W)]

    for c in comb_t:

        f = True
        for i in range(W - 2):
            if c[i] == c[i + 1] == 1:
                f = False
                break

        if f:
            for i in range(W):

                if i - 1 >= 0 and c[i - 1] == 1:
                    comb[i][0] += 1
                elif i < W - 1 and c[i] == 1:
                    comb[i][2] += 1
                else:
                    comb[i][1] += 1

    dp = [[0 for _ in range(W)] for _ in range(H + 1)]
    dp[0][0] = 1

    for y in range(H):
        for x in range(W):

            now = dp[y][x]
            dp[y + 1][x] += now * comb[x][1]
            dp[y + 1][x] %= mod
            if 0 <= x - 1 < W:
                dp[y + 1][x - 1] += now * comb[x][0]
                dp[y + 1][x - 1] %= mod
            if 0 <= x + 1 < W:
                dp[y + 1][x + 1] += now * comb[x][2]
                dp[y + 1][x + 1] %= mod

    print(dp[H][K - 1])


if __name__ == '__main__':
    main()
