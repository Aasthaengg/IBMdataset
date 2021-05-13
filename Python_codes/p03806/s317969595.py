N , Ma, Mb = map(int, input().split())

a = [0] * N
b = [0] * N
c = [0] * N

for i in range(N):
    a[i], b[i], c[i] = map(int, input().split())

# TLEになってしまうためinfを5000とかで設定する
INF = 5000

# 最小値を求める問題なのでinfで初期化
# dp[i][sun_a][sum_b]で考えていく
dp = [[[INF for _ in range(10 * N + 1)] for _ in range(10 * N + 1)] for _ in range(N+1)]

# 初期選択状態を0とする

dp[0][0][0] = 0
for i in range(N):
    for j in range(10*N+1):
        for k in range(10*N+1):
            if dp[i][j][k] == INF:
                continue
            
            # 選ばなかった場合
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
            # 選んだ場合
            dp[i+1][j+a[i]][k+b[i]] = min(dp[i+1][j+a[i]][k+b[i]], dp[i][j][k] + c[i])


ans = INF
# 0スタートは何を選んでいない状態となり最小値が0になってしまうため1から開始する

# TLEになったため変更
#for i in range(1,10 * N + 1):
#    for j in range(1,10 * N + 1):
#        if i * Mb != j * Ma:
#            continue
#        ans = min(ans, dp[N][i][j])
#

for i in range(1, 10*N+1):
        if i*Ma>10*N or i*Mb>10*N:
            break
        ans = min(ans, dp[N][i*Ma][i*Mb])

if ans == INF:
    print(-1)
else:
    print(ans)