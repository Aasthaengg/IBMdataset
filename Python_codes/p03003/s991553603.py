from collections import defaultdict

N, M = map(int, input().split())
S = [0] + list(map(int, input().split()))
T = [0] + list(map(int, input().split()))
mod = 10 ** 9 + 7
sum_dp = []
for i in range(N+1):
    sum_dp.append([0] * (M+1))

for i in range(1, N+1):
    for j in range(1, M+1):
        temp = 0
        if(S[i] == T[j]):
            temp = sum_dp[i-1][j-1] + 1
        sum_dp[i][j] = (sum_dp[i-1][j] + sum_dp[i][j-1] - sum_dp[i-1][j-1] + temp)
        sum_dp[i][j] %= mod
        
print(sum_dp[N][M] + 1)
