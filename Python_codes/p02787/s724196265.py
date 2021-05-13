import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, N, *AB = map(int, read().split())

    dp = [INF] * (H + 1)
    dp[0] = 0

    for a, b in zip(*[iter(AB)] * 2):
        for i in range(H + 1):
            dp[i] = min(dp[i], dp[max(i - a, 0)] + b)

    print(dp[H])
    return


if __name__ == '__main__':
    main()
