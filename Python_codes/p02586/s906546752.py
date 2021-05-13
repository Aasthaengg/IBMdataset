import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    R, C, K, *RCV = map(int, read().split())

    item = [[0] * C for _ in range(R)]
    for r, c, v in zip(*[iter(RCV)] * 3):
        item[r - 1][c - 1] = v

    dp = [0] * (C + 1)
    for i in range(R):
        value = [0] * 4
        for j in range(C):
            if value[0] < dp[j + 1]:
                value[0] = dp[j + 1]
            if item[i][j] > 0:
                for k in range(2, -1, -1):
                    if value[k + 1] < value[k] + item[i][j]:
                        value[k + 1] = value[k] + item[i][j]
            dp[j + 1] = max(value)

    print(dp[C])

    return


if __name__ == '__main__':
    main()
