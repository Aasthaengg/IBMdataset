if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))

    dp = [[10 ** 9 for j in range(2)] for i in range(n)]
    dp[0][0] = 1 # increase
    dp[0][1] = 1 # decrease

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            dp[i][0] = min(dp[i-1][0], dp[i-1][1] + 1)
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
        elif arr[i] < arr[i-1]:
            dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + 1
            dp[i][1] = min(dp[i-1][0] + 1, dp[i-1][1])
        else:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1]
    # print(dp)
    print(min(dp[-1]))