from itertools import permutations

N,M,R = map(int,input().split())
r = list(map(int,input().split()))

li = [[0 for i in range(N+1)]for j in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    li[a][b] = c
    li[b][a] = c

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

lin = all_pairs_shortest_paths(li)

pos = list(permutations(r))

mi = 10**18

for i in pos:
    l = 0
    for j in range(1,R):
        l += lin[i[j-1]][i[j]]
    mi = min(mi,l)

print(mi)