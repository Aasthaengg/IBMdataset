h, w, k = map(int, input().split())
dp = [1] + [0] * (w - 1)
mod = 1000000007
for _ in range(h):
    newdp = [0] * w
    for b in range(1 << (w - 1)):
        valid = True
        for i in range(w - 1):
            if (b >> i) & 3 == 3:
                valid = False
        if valid:
            for i in range(w):
                if (b >> i) & 1 != 0:
                    newdp[i + 1] = (newdp[i + 1] + dp[i]) % mod
                elif i > 0 and (b >> (i - 1)) & 1 != 0:
                    newdp[i - 1] = (newdp[i - 1] + dp[i]) % mod
                else:
                    newdp[i    ] = (newdp[i    ] + dp[i]) % mod
    dp = newdp
print(dp[k - 1])
