from itertools import product

S = input()
N = len(S)
MOD = 10**9 + 7

dp = {i: {j: 0 for j in range(3+1)} for i in range(N+1)}
for i, j in reversed(list(product(range(N+1), range(3+1)))):
    if i < N and j < 3:
        m1 = 3 if S[i] == '?' else 1
        m2 = 1 if S[i] == '?' or S[i] == ['A', 'B', 'C'][j] else 0
        dp[i][j] = m1*dp[i+1][j] + m2*dp[i+1][j+1]
    elif i < N and j == 3:
        dp[i][j] = 3*dp[i+1][j] if S[i] == '?' else dp[i+1][j]
    elif i == N and j == 3:
        dp[i][j] = 1
    dp[i][j] %= MOD
print(dp[0][0])