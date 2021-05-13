def main():
    N = int(input())
    dp = [N] * (N+1)
    dp[0] = 0

    for i in range(1, N+1):
        j = 1
        while j <= N:
            dp[i] = min(dp[i], dp[i-j]+1)
            j *= 6
        j = 1
        while j <= N:
            dp[i] = min(dp[i], dp[i-j]+1)
            j *= 9
    
    res = dp[N]
    print(res)



if __name__ == "__main__":
    main()