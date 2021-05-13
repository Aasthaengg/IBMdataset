MOD = 10**9+7
h, w, K = map(int, input().split())
n = w-1
dp = [[0] * w for _ in range(h+1)]
dp[0][0] = 1

def judge(edge):
    for i in range(1, n):
        if edge[i] and edge[i-1]: return False
    return True

for i in range(1, h+1):
    for j in range(w):
        for k in range(2**n):
            edge = [1 & (k >> l) for l in range(n)]
            if not judge(edge): continue
            if j < w-1 and edge[j]: dp[i][j] += dp[i-1][j+1]
            if j > 0 and edge[j-1]: dp[i][j] += dp[i-1][j-1]
            edge.append(0)
            if not edge[j] and not edge[j-1]:
                dp[i][j] += dp[i-1][j]

            dp[i][j] %= MOD

print(dp[h][K-1])
