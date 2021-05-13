def main():
    h,w = map(int, input().split())
    maze = [input() for _ in range(h)]
    dp = [[1] * w for _ in range(h)]
    for i,s in enumerate(maze):
        for j,t in enumerate(s):
            if t == '#':
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[i][j] == 1
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    ans = dp[h-1][w-1] % (10**9+7)
    print(ans)

if __name__ == '__main__':
    main()