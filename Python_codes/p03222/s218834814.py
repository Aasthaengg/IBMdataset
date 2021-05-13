h, w, K = map(int, raw_input().split())
dp = [[0]*w for i in range(h+1)]
dp[0][0] = 1
MOD = 10**9+7
def valid_mask():
    res = []
    for mask in range(1 << (w-1)):
        invalid = False
        for k in range(w-2):
            if (mask & 1 << k) > 0 and (mask & 1 << (k+1)) > 0:
                invalid = True
                break
        if not invalid:
            res.append(mask)
    return res

masks = valid_mask()

for i in range(h):
    for j in range(w):
        for mask in masks:
            if j < w-1 and (mask & 1 << j) > 0:
                dp[i+1][j+1] = (dp[i][j] + dp[i+1][j+1]) % MOD
            elif j - 1 >= 0 and (mask & (1 << (j-1))) > 0:
                dp[i+1][j-1] = (dp[i][j] + dp[i+1][j-1]) % MOD
            else:
                dp[i+1][j] = (dp[i][j] + dp[i+1][j])% MOD

print dp[h][K-1] % MOD