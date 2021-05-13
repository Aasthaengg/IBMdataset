MOD = 10**9 + 7
N = int(input())
C = [int(input()) for _ in range(N)]
dp = [0]*(N+1)
lis = [-1] * (2 * 10**5 + 1)
dp[0] = 1
lis[C[0]] = 0
for i,c in enumerate(C[1:],1):
    prev_i = lis[c]
    dp[i] = dp[i-1]
    if prev_i != i-1:
        dp[i] += dp[prev_i]
        dp[i] %= MOD
    lis[c] = i
answer = dp[N-1]
print(answer)