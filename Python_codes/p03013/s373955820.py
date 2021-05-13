# ABC129 C

MOD = 10**9 + 7
n, m = map(int, input().split())
a_l = [int(input()) for _ in range(m)]

dp = [0] * (n+1)
dp[0] = 1
k = 0
if m > 0 and a_l[0] == 1:
    k = min(k+1, m-1)
else:
    dp[1] = 1

for i in range(2, n+1):
    if m > 0 and i == a_l[k]:
        k = min(k+1, m-1)
        continue
    dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
print(dp[n])