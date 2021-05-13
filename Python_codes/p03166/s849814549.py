from collections import defaultdict, deque
n,m = map(int,input().split())
d = defaultdict(list)
deg = [0]*n  # 各頂点の入次数

for i in range(m):
    x,y = map(int,input().split())
    d[x-1].append(y-1)
    deg[y-1] += 1

que = deque([])
for v in range(n):
    if deg[v] == 0:
        que.append(v)

dp = [0]*100100

while que:
    v = que.popleft()
    for nv in d[v]:
        deg[nv] -= 1  # エッジ(v,nv)を破壊
        if deg[nv] == 0:
            que.append(nv)  # 入次数が0になったらキューに追加
            dp[nv] = max(dp[nv],dp[v]+1)  # ソースからnvまでの最長距離を確定

res = 0
for v in range(n):
    res = max(res,dp[v])
print(res)