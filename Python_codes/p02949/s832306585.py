#単一始点最短経路問題
#負の辺があっても動作する

#最短経路を求める
#計算量O(N * M)

INF = 10 ** 15
#入力
# N = int(input()) #頂点の数
# M = int(input()) #辺の数
N, M, P = map(int, input().split())

# 入力は1-index
# 内部で0-indexにして処理
G = []
for _ in range(M): #M個の辺の情報を受け取る
    l, r, s = map(int, input().split()) #lからrへ重みsの辺が存在
    G += [[l-1, r-1, -(s-P)]] #有向グラフのときはここだけ
    # G += [[r-1, l-1, s]] #無向グラフのときはこの行も必要

#メイン文
d = [INF] * N #最短距離を記録しておくリスト
# prev = [-1] * N
negative = [False] * N
def restore(g): #gまでの最短経路を復元
    path = []
    g -= 1 #0-indexに直す
    path.append(g)
    g = prev[g]
    count = 0
    while g != -1:
        # print ('C')
        path.append(g)
        g = prev[g]
        count += 1
        if count == N + 2:
            break
    path.reverse()
    return path

def shortest_path(s): #S番目の頂点から各頂点への最短距離を求める
    s -= 1
    for i in range(N):
        d[i] = INF
    d[s] = 0
    count = 0
    while count < N - 1:
        count += 1
        for i in range(M): #無向グラフのときは辺は実質的には2倍
            e = G[i]
            if d[e[0]] != INF and d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
    
    count = 0
    while count < N:
        count += 1
        for i in range(M): #無向グラフのときは辺は実質的には2倍
            e = G[i]
            if d[e[0]] == INF:
                continue
            if d[e[0]] != INF and d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                negative[e[1]] = True
            if negative[e[0]]:
                negative[e[1]] = True


#呼び出しスタート地点を入れる
shortest_path(1)
if negative[N - 1]:
    print (-1)
    # print (d)
    exit()
# print (d)
else:
    print (max(0, -d[N - 1]))