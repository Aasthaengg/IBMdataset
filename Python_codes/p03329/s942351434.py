n = int(input())
dp = [n] * (n+1)
dp[0] = 0
# 貰うdp -- dp[i] に遷移を集める
for i in range(1,n+1):
    pow6 = 1
    while pow6 <= i: # i円を実現できるか、を回す
        dp[i] = min(dp[i],dp[i-pow6] + 1)
        pow6 *= 6
    pow9 = 1
    while pow9 <= i:
        dp[i] = min(dp[i], dp[i-pow9] + 1)
        pow9 *= 9
print(dp[n])
