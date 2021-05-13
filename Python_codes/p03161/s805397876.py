import numpy as np

N, K = list(map(int, input().split()))
h = np.array(list(map(int, input().split())))

dp = np.array([np.inf] * N)
dp[0] = 0
dp[1] = abs(h[1]-h[0])
for i in range(2,N):
        if i - K >= 0:
            dp[i] = min(dp[i-K:i]+abs(h[i]-h[i-K:i]))
        else:
            dp[i] = min(dp[0:i]+abs(h[i]-h[0:i]))
print(int(dp[N-1]))