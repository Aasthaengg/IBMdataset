n,m = map(int,input().split())
a = {int(input()) for _ in range(m)}
mod = 10**9 + 7

dp = [0]*(n+1)
dp[0] = 1
    
for i in range(1,n+1):
    if i in a:
        continue
    x = dp[i-1] 
    if i > 1:
        x += dp[i-2]
    dp[i] = x
ans = dp[n] % mod
print(ans)