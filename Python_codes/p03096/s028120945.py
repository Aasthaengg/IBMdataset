n = int(input())
c = [int(input()) for _ in range(n)]
v_c = []
MOD = 10**9+7

for i,v in enumerate(c):
    if i > 0 and v == c[i-1]:
        continue
    v_c.append(v)

dp = [1]*(n+1)
color_cnt = [-1]*(2*10**5+5)
for i in range(1, len(v_c)+1):
    color = v_c[i-1]
    if color_cnt[color] > 0:
        dp[i] = dp[i-1] + dp[color_cnt[color]]
    else:
        dp[i] = dp[i-1]
    dp[i] %= MOD
    color_cnt[color] = i
print(dp[len(v_c)])
