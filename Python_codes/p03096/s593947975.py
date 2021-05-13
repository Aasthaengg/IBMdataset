from collections import defaultdict
mod = 10**9+7
n = int(input())
c = [0]
d = defaultdict(list)
r = defaultdict(int)

idx = 1
for i in range(n):
    tmp = int(input())
    if c[-1] != tmp:
        if d[tmp]:
            r[idx] = d[tmp][-1]
        d[tmp].append(idx)
        c.append(tmp)
        idx += 1

n = len(c)
dp = [0]*(n)
dp[0] = 1
for i in range(1, n):
    dp[i] = dp[i-1]
    if r[i]:
        dp[i] += dp[r[i]]
    dp[i] %= mod
print(dp[-1])
