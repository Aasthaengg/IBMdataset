mod = 10 ** 9 + 7
h, w, k = map(int, input().split())
k -= 1

dp = [0] * w
dp[0] = 1
ndp = [0] * w

for _ in range(h):
    for bits in range(1 << w - 1):
        if '11' in bin(bits): continue
        to = list(range(w))
        for i in range(w - 1):
            if (bits >> i) & 1:
                to[i], to[i + 1] = to[i + 1], to[i]
        for i in range(w):
            ndp[to[i]] += dp[i]
            ndp[to[i]] %= mod
    dp = ndp
    ndp = [0] * w
print(dp[k])
