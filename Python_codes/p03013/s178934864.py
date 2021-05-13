MOD=10**9+7
n,m = list(map(int, input().split()))
a = set([int(input()) for _ in range(m)])

dp = [0] * (n+1)

dp[0] = 1
dp[1] = int(1 not in a)
for step in range(2, n+1):
    if dp[step-1]==0 and dp[step-2]==0:
        break
    if step not in a:
        dp[step] = (dp[step-1] + dp[step-2])%MOD
    else:
        dp[step] = 0
        
print(dp[-1])