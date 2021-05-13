n = int(input())
mod = pow(10, 9) + 7
x = 0
c = []
for _ in range(n):
    y = int(input())
    if not x == y:
        c.append(y)
    x = y
m = len(c)
last = [-1] * (2 * pow(10, 5) + 5)
dp = [0] * m
dpsum = [0] * m
for i in range(m):
    if not last[c[i]] == -1:
        dp[i] = dpsum[last[c[i]]] + 1
    dpsum[i] = dp[i] + dpsum[max(i - 1, 0)]
    dpsum[i] %= mod
    last[c[i]] = i
ans = (dpsum[-1] + 1) % mod
print(ans)