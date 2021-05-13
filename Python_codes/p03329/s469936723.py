n = int(input())

# 6**7 # 279936
# 9**6 # 531441
c = [1] + [6**i for i in range(1,7)] + [9**i for i in range(1,6)]
c.sort()
#[1, 6, 9, 36, 81, 216, 729, 1296, 6561, 7776, 46656, 59049]
INF = 10 ** 10

dp = [INF] * (n + 1)
dp[0] = 0

for ci in c:
    for i in range(ci, n+1):
        dp[i] = min(dp[i], dp[i-ci] + 1)
print(dp[n])