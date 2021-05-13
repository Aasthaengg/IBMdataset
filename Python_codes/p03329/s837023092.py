import math

N = int(input())
dp= [0] * (N+1)

dp[0] = 0

for i in range(1,N+1):
    A = dp[i-1] + 1
    
    k = int(round(math.log(i, 6), 10))
    B = dp[i - 6 ** k] + 1
    
    k = int(round(math.log(i, 9), 10))
    C = dp[i - 9 ** k] + 1

    dp[i] = min(A,B,C)

print(dp[N])