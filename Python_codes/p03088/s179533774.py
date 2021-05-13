N = int(input())

MOD = 10 ** 9 + 7

# dp[n][i][j][k]: str[n:n+3]で(i,j,k)となる個数
dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N - 2)]

# 初期条件
for i in range(4):
    for j in range(4):
        for k in range(4):
            if i == 0 and j == 1 and k == 2: # ACG
                continue
            if i == 0 and j == 2 and k == 1: # AGC
                continue
            if i == 2 and j == 0 and k == 1: # GAC
                continue
            dp[0][i][j][k] = 1

# 配るDP
for n in range(N - 3):
    for i in range(4):
        for j in range(4):
            for k in range(4):

                # c: 次の文字
                for c in range(4):
                    if j == 0 and k == 1 and c == 2: # ?ACG
                        continue
                    if j == 0 and k == 2 and c == 1: # ?AGC
                        continue
                    if j == 2 and k == 0 and c == 1: # ?GAC
                        continue
                    if i == 0 and k == 2 and c == 1: # A?GC
                        continue
                    if i == 0 and j == 2 and c == 1: # AG?C
                        continue

                    dp[n+1][j][k][c] = (dp[n+1][j][k][c] + dp[n][i][j][k]) % MOD

ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans = (ans + dp[-1][i][j][k]) % MOD

print(ans)