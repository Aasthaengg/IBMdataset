def main():
    n, m = map(int, input().split())
    mo = list(map(int, input().split()))
    dp = [float("inf") for i in range(n + 2)]
    dp[0] = 0
    for i in range(n + 1):
        for j in mo:
            if i + j <= n:
                temp_index = i + j
                dp[temp_index] = min(dp[temp_index], dp[i] + 1)
    print(dp[n])


if __name__ == '__main__':
    main()

