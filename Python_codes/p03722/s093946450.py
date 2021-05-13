n,m=map(int,input().split())
g=[[] for _ in range(n)]
abc=[list(map(int,input().split())) for _ in range(m)]
abc=[[a-1,b-1,-c] for a,b,c in abc]


# https://img.atcoder.jp/abc061/editorial.pdf
# 上のD問題
# BellmanFord
# ベルマンフォード法
# edges:エッジ、有向エッジ[a,b,c]a->bのエッジでコストc
# num_v:頂点の数
# source:始点
def BellmanFord(edges,num_v,source):
  #グラフの初期化
  inf=float("inf")
  dist=[inf for i in range(num_v)]
  dist[source]=0  
  #辺の緩和をnum_v-1回繰り返す。num_v回目に辺の緩和があればそれは閉路。-1を返す。
  for i in range(num_v-1):
    for edge in edges:
      if dist[edge[0]] != inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
        dist[edge[1]] = dist[edge[0]] + edge[2]
        if i==num_v-1: return -1
  #閉路に含まれる頂点を探す。
  negative=[False]*n
  for i in range(num_v):
    for edge in edges:
      if negative[edge[0]]:negative[edge[1]]=True
      if dist[edge[0]] != inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
        negative[edge[1]] = True
  return dist[n-1],negative[n-1]
ans,nega=BellmanFord(abc,n,0)
if nega:
  print('inf')
else:
  print(-ans)
