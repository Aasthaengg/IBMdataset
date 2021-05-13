#ABC142-E Get Everything
"""
宝箱の制約が12個なので、これの状態を集合とする.
全ての状態について、(これはdpテーブルの状態ではない)
全ての鍵について考え、
この2つの状態のorで得られる状態sのdpテーブルをcost最小値で更新
そのようにして得られるdp[-1]が答えで、
この時O(2^N*M)がだいたい60**6なのでギリok
"""
import sys
readline = sys.stdin.buffer.readline

n,m = map(int,readline().split())
INF = 10**10
cost_len_key = []
for i in range(m):
    a,b = map(int,readline().split())
    lst1 = list(map(int,readline().split()))
    res = 0
    for j in lst1:
        res += 1<<(j-1)
    cost_len_key.append([a,b,res])

#dp:状態s(か、s以上)の箱を開けた場合の最小コスト
dp = [INF for _ in range(1<<n)]
dp[0] = 0 #1つも開けていない状態はコスト0

for i in range(1<<n): #すべての状態について回す
    for j in cost_len_key: #すべての鍵について回す
        s = i|j[2] #状態=iの状態の宝箱が空いているときに、鍵jで追加して開ける時の状態
        dp[s] = min(dp[s],dp[i]+j[0]) #そのような状態の時のコストの最小値

ans = dp[-1] #全部の鍵が空いた時の最小コストが答え
if ans < INF:
    print(ans)
else:
    print(-1)