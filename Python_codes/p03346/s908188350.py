n = int(input())
d = {0:n}
for i in range(n):
    p = int(input())
    d[p] = i

dp = [1]*(n+1)
for i in range(n):
    if d[i+1] > d[i]:
        dp[i+1] = dp[i] + 1
print(n - max(dp))