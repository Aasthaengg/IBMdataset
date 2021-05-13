from copy import copy
N = int(input())
P = list(map(float,input().split()))
dp = [0. for i in range(N+1)]
for i in range(N):
    if i == 0:
        dp[0] = 1. - P[i]
        dp[1] = P[i]
    else:
        new_dp = copy(dp)
        for j in range(N+1):
            if j == 0:
                new_dp[j] = dp[j]*(1-P[i])
            else:
                new_dp[j] = dp[j]*(1-P[i]) + dp[j-1]*(P[i])
        dp = copy(new_dp)
print(sum(dp[N//2+1:]))