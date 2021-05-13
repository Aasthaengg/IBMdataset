N = int(input())

a = []

# 1
a.append(1)

# 6**n
b = 6
while b <= N:
    a.append(b)
    b *= 6

# 9**n
b = 9
while b <= N:
    a.append(b)
    b *= 9

a.sort()

dp = [N] * (N+1)
dp[0] = 0
for i in range(N):
    for j in a:
        if i+j > N:
            break
        dp[i+j] = min(dp[i]+1, dp[i+j])
print(dp[N])
