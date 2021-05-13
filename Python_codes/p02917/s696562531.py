n = int(input())
b = list(map(int,input().split()))

dp = [10**8]*n

for i in range(n-1):
    if dp[i] > b[i] :
        dp[i] = b[i]
    if dp[i+1] > b[i] :
        dp[i+1] = b[i]

print(sum(dp))
