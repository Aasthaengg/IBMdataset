N,K=map(int, input().split())
hs=list(map(int, input().split()))

dp = [-100 for _ in range(N)]
dp[0] = 0
dp[1] = abs(hs[1]-hs[0])

for i in range(2,N):
    num = max(0, i-K)
    dp[i] = min([abs(hs[i]-hs[j])+dp[j]\
            for j in range(num, i)])

print(dp[-1])
