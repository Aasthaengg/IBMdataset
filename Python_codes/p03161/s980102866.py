if __name__ == '__main__':

    n,k = map(int,input().split())
    h = list(map(int,input().split()))

    #TLE pypy
    INF = 10**9
    dp = [INF] * (n+1)
    dp[0] = 0
    k = min(k,n)
    for i in range(1,n):
        for j in range(1,k+1):
            dp[i] = min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))
    print(dp[n-1])

