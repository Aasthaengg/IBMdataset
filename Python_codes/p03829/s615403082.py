def main():
    n, a, b = list(map(int, input().split()))
    X = list(map(int, input().split()))
    INF = float('inf')
    dp = [0] * n
    for i in range(1, n):
        dp[i] = dp[i - 1] + min(a * (X[i] - X[i - 1]), b)
    print(dp[n - 1])

if __name__ == '__main__':
    main()
