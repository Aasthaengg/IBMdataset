from sys import stdin
n,k = map(int,stdin.readline().split())
h = list(map(int,stdin.readline().split()))
dp = [0]
for i in range(1,n):
    x = 10**10
    for j in range(max(0,i-k),i):
        x = min(x,dp[j]+abs(h[j]-h[i]))
    dp.append(x)
print(dp[-1])