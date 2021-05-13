n = int(input())
a = list(map(int, input().split()))

dp = [0]*n

for i in range(1,n):
    if a[i-1] >= a[i]:
        dp[i] += dp[i-1]+1

print(max(dp))