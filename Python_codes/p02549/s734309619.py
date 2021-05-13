N, K = map(int, input().split())
mod = 998244353

L = []
for _ in range(K):
    a, b = map(int, input().split())
    b += 1
    L.append([a, b])

ruiwa = [0] * (N + 1)
dp = [0] * (N + 1)
dp[1] = 1
ruiwa[1] = 1
for i in range(2, N + 1):
    for l, r in L:
        l = i - l
        r = i - r
        l, r = r, l
        if r < 0:
            continue
        elif l >= 0:
            # print(ruiwa, r, l)
            dp[i] += (ruiwa[r] - ruiwa[l]) % mod
        else:
            dp[i] += ruiwa[r] % mod
    ruiwa[i] = (ruiwa[i - 1] + dp[i]) % mod

print(dp[-1] % mod)
