n, m = map(int, input().split())
G = [[] for _ in range(n)]
deg = [0] * n # 各頂点の入力次数
for _ in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    G[x].append(y)
    deg[y] += 1

from collections import deque
# 入力次数が0の頂点をBFSの開始点とする
q = deque([])
for i in range(n):
    if deg[i] == 0:
        q.append(i)
dp = [0] * n

while q:
    v = q.popleft()

    for nv in G[v]:
        # vからnvへの入力を削除
        deg[nv] -= 1
        if deg[nv] == 0:
            q.append(nv)
            dp[nv] = max(dp[nv], dp[v]+1)
    
print(max(dp))
