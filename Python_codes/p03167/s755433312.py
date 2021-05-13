H, W = map(int, input().split())

A_map = []
for i in range(H):
    A_str = input()
    A_map.append(A_str)

MOD = 10**9 + 7

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
dire = [[1,0], [0,1]] #下　右

for i in range(H):
    for j in range(W):
        if A_map[i][j] == '#':
            continue
        for k in dire:
            if 0 <= i+k[0] <= H-1 and  0 <= j+k[1] <= W-1:
                if A_map[i+k[0]][j+k[1]] == '.':
                    dp[i+k[0]][j+k[1]] +=  dp[i][j]%MOD
                    dp[i+k[0]][j+k[1]] %= MOD
#print(dp)
print(dp[H-1][W-1]%MOD)