def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    INF = 10**12
    dp = [INF] * (N+1)
    dp[1] = 0
    for i in range(1,N):
        for j in range(1,K+1):
            if i+j > N:
                break
            else:
                dp[i+j] = min(dp[i+j],dp[i]+abs(h[i-1]-h[i+j-1]))
    print(dp[N])

if __name__ == "__main__":
    main()