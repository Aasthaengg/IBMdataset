S = int(input())

mod = 10**9 + 7
dp = [0, 0, 0, 1]
for i in range(4, S+1):
    dp.append((dp[-1]+dp[-3])%mod)
print(dp[S])