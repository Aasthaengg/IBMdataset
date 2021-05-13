N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

# 移動量が最大2から最大Kになっただけ
# でもちょっとめんどい
# K回比較, を適当に関数にしとくことでforで回せるようになるらしい

dp=[float("inf")]*N
dp[0]=0
for i in range(1,N):
    for j in range(K):
        if i>j:
            dp[i] = min(dp[i], dp[i-j-1] + abs(H[i] - H[i-j-1]))
        # print(dp[i])
    # print(dp)
print(dp[N-1])