import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from operator import itemgetter

    n, t = list(map(int, readline().split()))
    mat = [list(map(int, readline().split())) for _ in range(n)]
    dp1 = [[0] * t for _ in range(n + 2)]
    dp2 = [[0] * t for _ in range(n + 2)]

    for i, vec in enumerate(mat):
        a = vec[0]
        b = vec[1]
        for time in range(t):
            if time + a < t:
                dp1[i + 1][time + a] = max(dp1[i][time + a], dp1[i][time] + b)
            dp1[i + 1][time] = max(dp1[i][time], dp1[i + 1][time])

    for j, vec in enumerate(mat[::-1]):
        i = n + 1 - j
        a = vec[0]
        b = vec[1]
        for time in range(t):
            if time + a < t:
                dp2[i - 1][time + a] = max(dp2[i][time + a], dp2[i][time] + b)
            dp2[i - 1][time] = max(dp2[i][time], dp2[i - 1][time])

    ans = 0
    for i, vec in enumerate(mat, 1):
        val = vec[1]
        for j in range(t):
            temp = dp1[i - 1][j] + dp2[i + 1][t - j - 1] + val
            ans = max(ans, temp)

    print(ans)


if __name__ == '__main__':
    main()
