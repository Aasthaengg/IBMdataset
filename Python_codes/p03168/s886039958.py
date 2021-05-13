import numpy as np
n = int(input())
p = list(map(float, input().split()))

dp = np.zeros(len(p)+1)
dp[0] = 1 - p[0]
dp[1] = p[0]

for i in range(1, len(p)):
    ura = dp * (1 - p[i])
    omote = np.append(np.zeros(1), dp[:-1] * p[i])
    dp = ura + omote

print(np.sum(dp[len(p)//2+1:]))