mod = 10 ** 9 + 7
H, W, K = map(int, input().split())
K -= 1
dp = [0] * W
dp[0] = 1
ndp = [0] * W
for r in range(H):
    for i in range(1 << (W - 1)):
        if '11' in bin(i): continue
        perm = [i for i in range(W)]
        for j in range(W - 1):
            if (i >> j) & 1:
                perm[j], perm[j + 1] = perm[j + 1], perm[j]
        for j in range(W):
            next_line = perm[j]
            ndp[next_line] += dp[j]
            ndp[next_line] %= mod
    dp = ndp.copy()
    ndp = [0] * W
print(dp[K])
