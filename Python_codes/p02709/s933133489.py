N = int(input())
A = [(a, i) for i, a in enumerate(map(int, input().split()), start=1)]#(Ai,i)を作成 iはスタート位置
A.sort(reverse=True)#Aiが大きい順にソート

dp = [[0] * (N + 1) for _ in range(N + 1)]
#dp[l][r]=l人は左、r人は右に配置した時の最大スコア

for s, (a, i) in enumerate(A):#Ai大きい順にs人動かした場合
    for l in range(s + 1):#0~s人うごかした時を考える s=l+r。
        r = s - l
        L = dp[l][r] + a * (i - (l + 1))
        R = dp[l][r] + a * (N - r - i)

        if dp[l + 1][r] < L:#最大値の更新
            dp[l + 1][r] = L
        if dp[l][r + 1] < R:
            dp[l][r + 1] = R

ans = 0
for i in range(N + 1):#Ansは左にi,右にN-i動かしたときの最大値、の中の最大値
    ans = max(ans, dp[i][N - i])
print(ans)