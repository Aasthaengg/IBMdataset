n, s = map(int, input().split())
a = list(map(int, input().split()))

mod = 998244353

pows = [1]
for i in range(10000):
    pows.append((pows[-1] * 2) % mod)

dp = [0] * (s + 1)
dp[0] = 1
if a[0] <= s:
    dp[a[0]] = 1

for i in range(1, n):
    dp_new = [0] * (s + 1)
    dp_new[0] = 1
    for j in range(1, s + 1):
        dp_new[j] = dp[j] * 2

        if j - a[i] > 0:
            dp_new[j] += dp[j-a[i]]
        elif j == a[i]:
            dp_new[j] += pows[i]
        dp_new[j] %= mod

    dp = dp_new

print(dp[-1])
