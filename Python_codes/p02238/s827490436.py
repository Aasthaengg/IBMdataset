# DFS(再帰） v:頂点
def DFS(v,dis,fin):
  global time
  # 訪問したので発見時刻を記入
  dis[v] = time
  time += 1
  
  # vに隣接している頂点をみる
  for u in V[v]:
    if dis[u] is None:
      DFS(u,dis,fin)
  
  # 処理が完了したので完了時刻を記入
  fin[v] = time
  time += 1
  
n = int(input())
# 0番目を始点として初期化
V = [[i for i in range(n)]]

for i in range(n):
  _, __, *a = map(int, input().split())
  V.append(a)

dis = [None]*(n+1)# 頂点を発見した時刻
fin = [None]*(n+1)# 頂点の完了時刻
time = 0
DFS(0,dis,fin)

for i in range(1,n+1):
  print(i, dis[i], fin[i])
