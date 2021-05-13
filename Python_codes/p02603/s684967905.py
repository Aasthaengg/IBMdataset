n = int(input())
a = list(map(int, input().split()))

# DP
# dp[i]: i日目の所持金の最大値（持ち株は売る）
dp = [0] * n
dp[0] = 1000

# dp[1] = 0日目に全部買って1日目に全部売る or 0日目から何もしない
# dp[2] = 0 or 1日目に全部買って2日目に全部売る or 1日目から何もしない
# dp[i+1] + 0~i日目のどこかで全部買ってi+1日目に全部売る or i日目から何もしない
for i in range(n):
    if i == 0:
        dp[i] = 1000
        continue
    
    dp[i] = dp[i-1]
    for j in range(i):
        # j日目に全部買ってi日目に全部売る
        dp[i] = max(dp[i], (dp[j] // a[j]) * a[i] + dp[j] % a[j])
    
print(dp[n-1])