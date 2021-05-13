n = int(input())
p = list(map(float, input().split()))
dp = [0]*(n+2)
dp[1] = 1
for i in p:
    newdp = dp[:]
    for j in range(n+1):
        newdp[j+1] = dp[j]*i + dp[j+1]*(1-i)
    dp = newdp

print(sum(dp[n//2+2:]))