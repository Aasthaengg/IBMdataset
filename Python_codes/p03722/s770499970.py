#Nは頂点数, Mは辺数(2 <= N <= 1000, 1 <= M <= min(N(N-1, 2000)))
#頂点1から頂点Nに移動して、移動スコアを最大にする
#->移動スコアを正負反転させれば最短経路問題
#->負閉路を考慮してベルマンフォード法を利用
INF = 1 << 50

N,M = map(int,input().split())

#辺を登録
Sides = []
for i in range (M):
    Side = list(map(int,input().split()))
    Sides.append(Side)
#コストを反転
    Sides[i][2] = Sides[i][2] * (-1)

#各頂点の最短距離を初期化
Vertexes = [INF]*(N+1)
Vertexes[1] = 0

#負閉路のチェック用
negative = [False] * (N+1)

#ベルマンフォード法による最短距離探索
for count in range(N):
    for i in range(M):
        from_v = Sides[i][0]
        to_v = Sides[i][1]
        cost = Sides[i][2]
        if (Vertexes[to_v] > Vertexes[from_v]+cost):
            if(count==N-1):
                negative[to_v] = True
            else:
                Vertexes[to_v] = Vertexes[from_v]+cost

#負閉路の確認
for count in range(N-1):
    flag = 0
    for i in range(M):
        from_v = Sides[i][0]
        to_v = Sides[i][1]
        if negative[from_v] :
            negative[to_v] = True
            flag = 1
    #if flag ==0:
     #   break

if negative[N]:
    print('inf')
else:
    print(-Vertexes[N])