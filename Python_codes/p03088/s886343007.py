N = int(input())
mod = 10 ** 9 + 7

# 直大さんの解説風
dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
dp[0][3][3][3] = 1

for Length in range(N):
    for i in range(4):
        for j in range(4):
            for k in range(4):

                if dp[Length][i][j][k] == 0:
                    continue

                for d in range(4):  # 追加する文字
                    if d == 1 and j == 0 and k == 2:
                        continue
                    if d == 2:
                        if j == 0 and k == 1:
                            continue
                        if j == 1 and k == 0:
                            continue
                        if i == 0 and k == 1:
                            continue
                        if i == 0 and j == 1:
                            continue

                    dp[Length + 1][j][k][d] += dp[Length][i][j][k]
                    dp[Length + 1][j][k][d] %= mod

ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans = (ans + dp[N][i][j][k]) % mod
print(ans)
