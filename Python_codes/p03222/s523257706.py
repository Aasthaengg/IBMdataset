H, W, K = [int(_) for _ in input().split()]

pat = set()


def make_pat(v):
    if v in pat: return
    a = v
    while a > 0:
        if a & 1 and a & 2:
            return
        a = a >> 1

    pat.add(v)
    for i in range(W - 1):
        a = 1 << i
        if a & v: continue
        make_pat(a | v)


make_pat(0)
# print(pat)

dp = [[0] * (W + 5) for _ in range(H + 1)]

dp[0][0] = 1
MOD = 10 ** 9 + 7

for i in range(H):
    for line in pat:
        for j in range(W):
            # j 番目の棒を考える
            if line & (1 << j):  # 右側
                dp[i + 1][j + 1] += dp[i][j] % MOD
            elif j > 0 and line & (1 << (j - 1)):  # 左側
                dp[i + 1][j - 1] += dp[i][j] % MOD
            else:
                dp[i + 1][j] += dp[i][j] % MOD
print(dp[H][K - 1] % MOD)
