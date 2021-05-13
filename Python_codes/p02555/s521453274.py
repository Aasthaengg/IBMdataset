# 【abc-178】個人的ふりかえり（A〜E）
# https://qiita.com/nyororingo/items/d372d1ff3f690b0d1fe2

S = int(input())
MOD = 10 ** 9 + 7
    
dp = [0] * (S + 1)
dp[0] = 1
for i in range(3, S + 1):
    #print(dp)
    #for j in range((i - 3) + 1):

        #dp[i] += dp[j]
        dp[i] = dp[i-1] +dp[i-3]
        dp[i] %= MOD
print(dp[S] % MOD)