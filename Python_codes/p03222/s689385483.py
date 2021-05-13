h, w, k = map(int, input().split())

MOD = 10**9 + 7
k -= 1

dp = [[0] * w for _ in range(h+1)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        for bit in range(1<<(w-1)):
            ok = True
            for _ in range(w-2):
                if not (bit + (bit<<1) == bit ^ (bit<<1)):
                    ok = False
            if not ok:
                continue
            ni = i+1; nj = j
            if (bit>>j) & 1:
                nj = j+1
            elif j > 0 and (bit>>(j-1)) & 1:
                nj = j-1
            dp[ni][nj] += dp[i][j]
            dp[ni][nj] %= MOD           

ans = dp[h][k]
ans %= MOD
print(ans)