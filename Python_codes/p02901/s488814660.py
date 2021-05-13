N,M = map(int,input().split())
AB, C = [], []
for _ in range(M):
    AB.append(tuple(int(i) for i in input().split()))
    C.append(sum(1<<(int(i)-1) for i in input().split()))

INF = 10**18

# dp[i]: 状態がbin(i)のときの費用の最小値
# bin(i)のj桁が1: j番目の宝箱を開けられる
dp = [INF] * (1<<N)

# 初期条件(全ての宝箱を開けられない)
dp[0] = 0

for i in range(1<<N):
    for (a, _), c in zip(AB,C):
        # 状態iで状態cにする鍵を買ったときの状態
        state = i | c
        dp[state] = min(dp[state], dp[i] + a)

if dp[-1] == INF:
    ans = -1
else:
    ans = dp[-1]
print(ans)