n = int(input())
c = []
for _ in range(n):
    c.append(int(input()))

mod = 10**9+7
dp = [0] * n
dp[0] = 1

pre = [-1] * n
tmp = [-1] * (2*10**5+10)

for i in range(n):
    pre[i] = tmp[c[i]-1]
    tmp[c[i]-1] = i

for i in range(1,n):
    dp[i] = dp[i-1]
    if pre[i] != -1 and c[i] != c[i-1]:
        dp[i] += dp[pre[i]]
        dp[i] %= mod

print(dp[-1])
