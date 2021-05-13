# I - Coins
N = int(input())
P = list(map(float,input().split()))

# dp[i][j]: 最初の i 枚のコインを投げたとき、表が j 回出る確率
dp = [[0]*(N+1) for _ in range(N+1)]

# 初期条件
# コインを 0 枚投げたとき、表が 0 回出る確率は 1
dp[0][0] = 1

# コインを i 枚投げたとき
for i in range(1,N+1):
    # 表が j 回出たとき
    for j in range(1,i+1):
        # コインが表のときの確率
        dp[i][j] += dp[i-1][j-1]*P[i-1]
        # コインが裏のときの確率
        dp[i][j-1] += dp[i-1][j-1]*(1-P[i-1])
    
# 半分以上表ときの確率
ans = 0
for j in range(N//2 + 1,N+1):
    ans += dp[N][j]
print(ans)