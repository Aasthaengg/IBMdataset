import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    a = [0] + list(map(int, readline().split()))
    dp = [0] * (n + 1)
    dp[0] = 1000

    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        for j in range(1, i):
            s = dp[j] // a[j]
            m = s * a[i] + dp[j] % a[j]
            dp[i] = max(dp[i], m)

    print(dp[n])


if __name__ == '__main__':
    main()
