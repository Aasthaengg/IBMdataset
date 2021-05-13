def solve(n, m, grid):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    mod = int(1e9+7)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i-1][j-1] == '#' or i == 1 and j == 1:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            dp[i][j] %= mod

    return dp[-1][-1]


def main():
    inp = lambda: [int(x) for x in input().split()]
    n, m = inp()
    grid = [input() for _ in range(n)]
    print(solve(n, m, grid))


if __name__ == '__main__':
    main()
