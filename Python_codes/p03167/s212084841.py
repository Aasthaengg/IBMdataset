H, W = map(int, input().split())
S = [[a for a in input()] for _ in range(H)]
mod = 10 ** 9 + 7
DP = [[0] * (W + 1) for _ in range(H+1)]
DP[1][1] = 1
for i in range(1, H+1):
    for j in range(1, W+1):
        if S[i-1][j-1] == '#':
            continue
        if i == 1 and j == 1:
            continue
        DP[i][j] = DP[i - 1][j] + DP[i][j - 1]
        DP[i][j] %= mod

print(DP[-1][-1])
