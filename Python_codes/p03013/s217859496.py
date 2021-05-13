def main():
    n,m = map(int,input().split())
    dp = [0 for i in range(n+1)]
    mod = 10**9+7
    for i in range(m):
        a = int(input())
        dp[a] = -1
    dp[0] = 1
    if dp[1]!=-1:
        dp[1] = 1
    for i in range(2,n+1):
        if dp[i]==-1:
            continue
        if dp[i-1]!=-1 and dp[i-2]!=-1:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] = dp[i]%mod
        elif dp[i-1]!=-1 and dp[i-2]==-1:
            dp[i] = dp[i-1]
        elif dp[i-1]==-1 and dp[i-2]!=-1:
            dp[i] = dp[i-2]
        else:
            dp[i] = 0
    print(dp[-1])

if __name__ == "__main__":
    main()
