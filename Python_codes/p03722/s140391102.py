n,m=map(int,input().split())
E=[list(map(int,input().split())) for i in range(m)]
INF=float("inf")
dist=[INF]*n
dist[0]=0
for i in range(n):
  for fr,to,cost in E:
    fr,to=fr-1,to-1
    # スコアの正負を逆にしてスコアを最小化することを考える
    cost*=-1
    if dist[fr]!=INF and dist[to]>dist[fr]+cost:
      dist[to]=dist[fr]+cost
      # 負経路の存在チェック
      # 一番最後に緩和（更新）が発生するとNG（負閉路の長さは頂点の個数以下なので）
      if i==n-1 and to==n-1:
        print("inf")
        exit(0)
print(-dist[-1])

