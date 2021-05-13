n = int(input())
c = [int(input()) for _ in range(n)]
m = 10**9+7

dp = [-1] * n
dp[0] = 1
last_dic = {}
for i in range(n):
    if c[i] in last_dic.keys() and i - last_dic[c[i]] >= 2:
        dp[i] = (dp[i-1] + dp[last_dic[c[i]]]) % m
    elif i:
        dp[i] = dp[i-1]
    last_dic[c[i]] = i
print(dp[-1])