# D - Number of Amidakuji

import itertools

H, W, K = map(int, input().split())
MOD = 10**9 + 7

if W == 1:
    print(1)
    exit()

# move[i][j] 左iから左jに移動できる横棒のパターン数
move = [[0]*W for _ in range(W)]
for horizontal_line_pattern in list(itertools.product([0,1], repeat=W-1)):
    for i in range(W-2):
        if horizontal_line_pattern[i] == 1 and horizontal_line_pattern[i+1] == 1:
            break
    else:
        for i in range(W-1):
            if horizontal_line_pattern[i] == 1:
                move[i][i+1] += 1
                move[i+1][i] += 1
            else:
                if i == 0:
                    move[0][0] += 1
                elif i == W-2:
                    move[W-1][W-1] += 1
                try:
                    if horizontal_line_pattern[i+1] == 0:
                        move[i+1][i+1] += 1
                except IndexError:
                    pass

# dp[i][j] 0段目左0から辿るとi段目の移動の後で左jに到達するようなアミダクジのパターン数
dp = [[0]*W for _ in range(H+1)]
dp[0][0] = 1

for i in range(1, H+1):
    for j in range(W):
        for k in [-1, 0, 1]:
            try:
                dp[i][j] += dp[i-1][j+k] * move[j][j+k]
                dp[i][j] %= MOD
            except IndexError:
                pass

print(dp[H][K-1])