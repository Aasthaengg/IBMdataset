N=int(input())
p=[float(i) for i in input().split()]

dp=[[] for _ in range(N)]

dp[0]=[1-p[0],p[0]]
for i in range(1,N):
    dp[i].append(dp[i-1][0]*(1-p[i]))
    for j in range(1,i+1):
        dp[i].append(dp[i-1][j]*(1-p[i])+dp[i-1][j-1]*p[i])
    dp[i].append(dp[i-1][-1]*p[i])

a=(N+1)//2
print(sum(dp[N-1][a:]))
