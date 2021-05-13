# Atcoder Problem Solving
# Sum Equals Xor
L = input()
ans = 0
mod = 10**9+7
L = L[::-1]
N = len(L)
dp = [0 for i in range(N+10)]

if L[0] == "0":
    dp[0] = 1
else:
    dp[0] = 3
for i in range(1, N):
    if L[i] == "1":
        dp[i] = 2*dp[i-1]+pow(3, i, mod)
        dp[i] %= mod
    else:
        dp[i] = dp[i-1]
print(dp[N-1] % mod)
