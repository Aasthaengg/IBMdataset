def main():
    n,k = map(int,input().split())
    h = [int(i) for i in input().split()]
    INF =  float('inf')
    dp = [INF for i in range(n)]
    dp[0] = 0
    dp[1] = abs(h[0]-h[1])
    for i in range(2,n):
        dp[i] = min(dp[i-j]+abs(h[i-j]-h[i]) for j in range(1,min(i,k)+1))
    print(dp[n-1])

main()
