import sys
n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
if n == 0:
    print(1)
    sys.exit()
elif n == 1:
    print(1)
    sys.exit()

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
