N, W = map(int, input().split())
w = []
v = []
for i in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
w_adjust = []
for i in range(N):
    w_adjust.append(w[i]-w[0])

a = w[0]
dp = [[[0 for i in range(N+1)] for j in range(N*3+10)] for k in range(N+1)]
#i個目までの物のうちk個選んで重さの和がjになる中での最大価値
for i in range(N):
    for j in range(3*N):
        for k in range(N):
            if j + w_adjust[i] > W - a*(k+1):
                dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
            else:
                dp[i+1][j+w_adjust[i]][k+1] = max(dp[i+1][j+w_adjust[i]][k+1], dp[i][j][k] + v[i])
                dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
ans = [0]
for i in range(1, N+1):
    if W - a*i >= 0 and W - a*i < N*3 + 3:
        ans.append(dp[N][W-a*i][i])

if W - a*N > N*3:
    things = W//w[0]
    if things > N:
        ans.append(sum(v))

elif len(ans) == 1:
    things = W//w[0]
    v.sort()
    v.reverse()
    ans_1 = 0
    for i in range(things):
        ans_1 += v[i]
    ans.append(ans_1)

print(max(ans))
