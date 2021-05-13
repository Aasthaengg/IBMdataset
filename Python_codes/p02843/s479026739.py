n = int(input())

dp = [0]*100001
dp[100],dp[101],dp[102],dp[103],dp[104],dp[105] = 1,1,1,1,1,1

for i in range(99896):
    if dp[i] == 1:
        dp[i+100],dp[i+101],dp[i+102],dp[i+103],dp[i+104],dp[i+105] = 1,1,1,1,1,1
print(dp[n])