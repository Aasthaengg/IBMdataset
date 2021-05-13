n,m = map(int,input().split())
li = [[0 for i in range(n)]for j in range(n)]
lis = []

def all_pairs_shortest_paths(W):
    inf = 10**18
    # 頂点の数
    n = len(W)
    # 結果を格納する行列を用意する
    res = [[0] * n for i in range(n)]
    # 用意した行列を初期化する
    for i in range(n):
        for j in range(i, n):
            if i == j:
                val = 0
            elif W[i][j]:
                val = W[i][j]
            else:
                val = inf
            res[i][j] = res[j][i] = val
    # 動的計画法ですべての超点間の最短距離を求める
    for k in range(n):
        for u in range(n):
            for v in range(n):
                res[u][v] = min(res[u][v], res[u][k] + res[k][v])
    return res

for _ in range(m):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    lis.append((a,b,c))
    li[a][b] = c
    li[b][a] = c

lin = all_pairs_shortest_paths(li)
point = 0

for path in lis:
    a,b,c = path
    flag = False
    for i in range(n):
        for j in range(n):
            if lin[i][a]+c+lin[b][j] == lin[i][j]:
                flag = True
    if not flag:
        point += 1

print(point)