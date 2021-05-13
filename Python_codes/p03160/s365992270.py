N=int(input())
hs=list(map(int, input().split()))

dp=[-100 for _ in range(N)]
dp[0]=0
dp[1]=abs(hs[1]-hs[0])+dp[0]


for i in range(2, N):
    tmp1 = abs(hs[i]-hs[i-1])+dp[i-1]
    tmp2 = abs(hs[i]-hs[i-2])+dp[i-2]
    dp[i] = min(tmp1, tmp2)
print(dp[-1])
