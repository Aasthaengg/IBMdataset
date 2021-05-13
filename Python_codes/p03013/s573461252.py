n, m = map(int, input().split())
issafe = [True] * (n +1)
for _ in range(m):
    a = int(input())
    issafe[a] = False

dp = [0] * (n + 1)
dp[0] = 1
if issafe[1]:
    dp[1] = 1

for i in range(2, n + 1):
    if  issafe[i - 1]:
        dp[i] = dp[i] + dp[i - 1]
    if issafe[i -  2]:
        dp[i] = dp[i - 2] + dp[i] 
    
    dp[i] %= 1000000007
    
print(dp[n])