N, T = map(int, input().split())
dp = [[0 for j in range(T)] for i in range(N)]
W = []
V = []
for i in range(N):
    w, v = map(int, input().split())
    W += [w]
    V += [v]
    
W, V = zip(*sorted(zip(W, V), key=lambda x: x[0]))
for i in range(N-1):
    for j in range(T):
        if j - W[i] < 0 :
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-W[i]] + V[i])
ans = 0
for i in range(N):
    ans = max(ans, dp[i][-1] + V[i])
print(ans)
