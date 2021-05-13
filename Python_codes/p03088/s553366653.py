import numpy as np
N = int(input())
p = 10 ** 9 + 7
dp = np.zeros((N + 1, 4, 4, 4), dtype = "int64")

# dp[0][c3][c2][c1] = 0 for all *** except c1=c2=c3=3
dp[0][3][3][3] = 1
for len in range(0, N):
    for c3 in range(0, 4):
        for c2 in range(0, 4):
            for c1 in range(0, 4):
                for newchar in range(0, 4):
                    # 条件を満たさないもの
                    if c2 == 0 and c1 == 1 and newchar == 2: continue
                    if c2 == 1 and c1 == 0 and newchar == 2: continue
                    if c2 == 0 and c1 == 2 and newchar == 1: continue
                    if c3 == 0 and c1 == 1 and newchar == 2: continue
                    if c3 == 0 and c2 == 1 and newchar == 2: continue
                    dp[len + 1][c2][c1][newchar] += dp[len][c3][c2][c1]
                    dp[len + 1][c2][c1][newchar] %= p

ans = dp[N].sum() % p
print(ans)