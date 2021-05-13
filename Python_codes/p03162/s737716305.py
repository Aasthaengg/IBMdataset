import numpy as np
n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())
dp = np.zeros((3, n+1), dtype=np.int)
for i in range(1, n+1):
    dp[0, i] = max(dp[1,i-1]+b[i-1], dp[2,i-1]+c[i-1])
    dp[1, i] = max(dp[0,i-1]+a[i-1], dp[2,i-1]+c[i-1])
    dp[2, i] = max(dp[0,i-1]+a[i-1], dp[1,i-1]+b[i-1])
print(max(dp[:, n]))