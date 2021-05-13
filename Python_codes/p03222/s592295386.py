from collections import defaultdict

H, W, K = map(int, input().split())
dp1 = [[0]*2 for _ in range(W)]
dp1[0][0] = 1

for i in range(W-1):
    dp1[i+1][0] = dp1[i][0]+dp1[i][1]
    dp1[i+1][1] = dp1[i][0]

d = defaultdict(int)
d[-1] = 1

for i in range(W):
    d[i] = dp1[i][0]+dp1[i][1]

dp2 = [[0]*W for _ in range(H+1)]
dp2[0][0] = 1
MOD = 10**9+7

for i in range(H):
    for j in range(W):
        for k in range(max(0, j-1), min(W-1, j+1)+1):
            l = min(j, k)-1
            r = W-2-max(j, k)
            dp2[i+1][k] += dp2[i][j]*d[l]*d[r]
            dp2[i+1][k] %= MOD

print(dp2[H][K-1])