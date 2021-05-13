def grid(mat: list):
    m = len(mat)
    n = len(mat[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if mat[i][j] == '.':
                if i > 0:
                    dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    return dp[m - 1][n - 1]%1000000007


if __name__ == '__main__':
    m, n = list(map(int, input().split()))
    mat = [[]] * m
    for i in range(m):
        mat[i] = [c for c in input()]
    print(grid(mat))
