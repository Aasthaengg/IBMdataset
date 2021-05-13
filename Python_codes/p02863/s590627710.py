import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from operator import itemgetter

    n, t = list(map(int, readline().split()))
    mat = [list(map(int, readline().split())) for _ in range(n)]
    mat.sort(key=itemgetter(0))
    dp = [[0] * t for _ in range(n + 1)]
    ans = 0

    for dish, vec in enumerate(mat):
        a = vec[0]
        b = vec[1]
        for time in range(t):
            dp[dish + 1][time] = max(dp[dish + 1][time], dp[dish][time])
            if time + a >= t:
                ans = max(ans, dp[dish][time] + b)
            else:
                dp[dish + 1][time + a] = max(dp[dish + 1][time + a], dp[dish][time] + b)

    ans = max(max(dp[n]), ans)
    print(ans)


if __name__ == '__main__':
    main()
