import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 998244353


def main():
    N, K, *LR = map(int, read().split())
    interval = [(l, r) for l, r in zip(*[iter(LR)] * 2)]

    dp = [0] * (N + 1)
    sdp = [0] * (N + 1)

    dp[0] = 1
    sdp[1] = 1

    for i in range(1, N):
        for l, r in interval:
            left = max(i - r, 0)
            right = max(i - l + 1, 0)
            dp[i] = (dp[i] + sdp[right] - sdp[left]) % MOD
        sdp[i + 1] = (sdp[i] + dp[i]) % MOD

    print(dp[N - 1])
    return


if __name__ == '__main__':
    main()
