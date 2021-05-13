n,m = map(int,input().split())
a = set([int(input()) for i in range(m)])
inf = 1000000007

dp = [0] * (n+1)
dp[0] = 1

if 1 not in a:
    dp[1] = 1
else:
    dp[1] = 0

for i in range(2,n+1):
    if i in a:
        continue
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= inf

print(dp[n])