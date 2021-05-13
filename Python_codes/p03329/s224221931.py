N = int(input())

dp = [10**5]*(N+1)
dp[0] = 0
dp[1] = 1
s = 6
n = 9
for i in range(2,N+1):
    if 6*s <= i:
        s *= 6
    if 9*n <= i:
        n *= 9
    if i < 6:
        dp[i] = dp[i-1]+1
    elif i < 9:
        dp[i] = min(dp[i-1], dp[i-s])+1
    else:
        dp[i] = min(dp[i-1], dp[i-s], dp[i-n])+1
print(dp[N])