n, m = map(int, input().split())
edges = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    edges[a-1][b-1] = 1
    edges[b-1][a-1] = 1

def dfs(start):
    if visited[start]:
        return
    visited[start] = 1
    for i in range(n):
        if edges[start][i]:
            dfs(i)

ans = m
# edgeを一つづつ見ていく
for i in range(n-1):
    for j in range(i+1, n):
        if not edges[i][j]:
            continue
        # エッジを削除した場合に、連結しているかをdfsで確認
        #   visited: 訪れたかどうかを表す変数
        visited = [0] * n
        edges[i][j] = 0
        edges[j][i] = 0
        dfs(0)
        # お片付け、削除したedgeを元に戻しておく
        edges[i][j] = 1
        edges[j][i] = 1
        # 全て訪れられていたら、そのエッジはなくても非連結にならないので、bridgeではない
        if sum(visited) == n:
            ans -=1

print(ans)