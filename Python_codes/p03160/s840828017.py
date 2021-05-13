n = int(input())
h = list(map(int, input().split(' ')))

dp = [0]*n

for i in range(1,n):
    if i>=2:
        dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))
    else:
        dp[i] = abs(h[1]-h[0])
print(dp[-1])