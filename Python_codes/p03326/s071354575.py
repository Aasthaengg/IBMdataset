import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())
    cakes = [(0, 0, 0)]
    for _ in range(N):
        x, y, z = map(int, input().split())
        cakes.append((x, y, z))

    """
    dp[n][m][t] = (1~n番目までのケーキからm個のケーキをタイプtで選んだ時の合計の最大値)
    と定める。ここでタイプとは
        t=0 -> val = x + y + z
        t=1 -> val = x + y - z
        t=2 -> val = x - y + z
        t=3 -> val = x - y - z
        t=4 -> val = -x + y + z
        t=5 -> val = -x + y - z
        t=6 -> val = -x - y + z
        t=7 -> val = -x - y - z
    どのタイプにせよ更新式は同じで、dp[n][m] = max(dp[n-1][m], dp[n-1][m-1] + (n番目のdp = [0]aaa))
    """

    dp = [[[0] * 8 for _ in range(M + 1)] for _ in range(N + 1)]
    for n in range(1, N + 1):
        x, y, z = cakes[n]
        for m in range(1, min(M + 1, n + 1)):
            if n == m:
                dp[n][m][0] = dp[n - 1][m - 1][0] + (x + y + z)
                dp[n][m][1] = dp[n - 1][m - 1][1] + (x + y - z)
                dp[n][m][2] = dp[n - 1][m - 1][2] + (x - y + z)
                dp[n][m][3] = dp[n - 1][m - 1][3] + (x - y - z)
                dp[n][m][4] = dp[n - 1][m - 1][4] + (-x + y + z)
                dp[n][m][5] = dp[n - 1][m - 1][5] + (-x + y - z)
                dp[n][m][6] = dp[n - 1][m - 1][6] + (-x - y + z)
                dp[n][m][7] = dp[n - 1][m - 1][7] + (-x - y - z)
            else:
                dp[n][m][0] = max(dp[n - 1][m][0], dp[n - 1][m - 1][0] + (x + y + z))
                dp[n][m][1] = max(dp[n - 1][m][1], dp[n - 1][m - 1][1] + (x + y - z))
                dp[n][m][2] = max(dp[n - 1][m][2], dp[n - 1][m - 1][2] + (x - y + z))
                dp[n][m][3] = max(dp[n - 1][m][3], dp[n - 1][m - 1][3] + (x - y - z))
                dp[n][m][4] = max(dp[n - 1][m][4], dp[n - 1][m - 1][4] + (-x + y + z))
                dp[n][m][5] = max(dp[n - 1][m][5], dp[n - 1][m - 1][5] + (-x + y - z))
                dp[n][m][6] = max(dp[n - 1][m][6], dp[n - 1][m - 1][6] + (-x - y + z))
                dp[n][m][7] = max(dp[n - 1][m][7], dp[n - 1][m - 1][7] + (-x - y - z))
    print(max(dp[N][M]))

if __name__ == "__main__":
    main()
