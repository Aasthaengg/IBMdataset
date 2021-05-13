import numpy as np

n = int(input())
tmp = [int(input()) for _ in range(n)]

c = [tmp[0]]
for x in tmp[1:]:
    if x != c[-1]:
        c.append(x)

c = np.array(c)

MOD = 10**9 + 7

# dpテーブル
dp = np.zeros(c.shape[0], dtype=np.int64)
dp[0] = 1

used = np.full(c.max() + 1, -1, dtype=np.int64)
used[c[0]] = 1

for i in range(1, c.shape[0]):
    if used[c[i]] == -1:
        dp[i] = dp[i - 1]
    else:
        dp[i] = (dp[i - 1] + dp[used[c[i]]]) % MOD
    used[c[i]] = i

print(dp[-1])