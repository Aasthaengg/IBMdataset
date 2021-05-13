n = int(input())
inf = float('inf')
dp = [inf]*(n+1)
dp[0] = 0
a = 1
b = 6
c = 9
for i in range(1,n+1):
    if i>=b*6:
        b*=6
    if i>=c*9:
        c*=9
    if i<6:
        dp[i] = i
    elif i<9:
        dp[i] = min(dp[i],dp[i-b]+1)
    else:
        dp[i] = min(dp[i],dp[i-b]+1,dp[i-c]+1)
print(dp[n])