N=int(input())
h=list(map(int, input().split()))
dp=[10000000000000]*(N+2)
#初期状態
dp[0]=0
#配るDP
for i in range(N):
    try:
        dp[i+1]=min(dp[i+1],dp[i]+abs(h[i+1]-h[i]))
    except IndexError:
        pass
    try:
        dp[i+2]=min(dp[i+2],dp[i]+abs(h[i+2]-h[i]))
    except IndexError:
        pass
print(dp[N-1])