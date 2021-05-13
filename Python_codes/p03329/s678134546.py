N = int(input())

dp = [float('inf')] * (N+1)
dest = [1]
dp[0] = 0
for i in range(1,10):
    if 6 ** i <= N:
        dp[6 ** i] = 1
        dest.append(6 ** i)
    else:
        break
    if 9 ** i <= N:
        dp[9 ** i] = 1
        dest.append(9 ** i)

for i in range(N+1):
    for j in dest:
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i-j]+1)
    
print(dp[N])