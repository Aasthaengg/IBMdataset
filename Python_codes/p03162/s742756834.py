import numpy as np

N = int(input())
plans = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(3)]

for j in range(N):
    for i_1 in range(3):
        for i_2 in range(3):
            if i_1 == i_2:
                continue
            dp[i_2][j+1] = max(dp[i_2][j+1], dp[i_1][j] + plans[j][i_2])

ans = np.array(dp)
print(ans[:, N].max())