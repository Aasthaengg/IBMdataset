import sys
sys.setrecursionlimit(500000) #これがないと再帰の回数オーバーでエラー出る。
N,M,P = map(int,input().split())
N-=1 #頂点番号を0スタートに。ただし頂点数はN+1となることに注意。
INF = float("inf")
edge = []
to = [[] for _ in range(N+1)] #普通に移動できる点
rto = [[] for _ in range(N+1)] #逆に戻れる点
reachablefrom = [False for _ in range(N+1)] #始点0から終点N-1へ行けるかチェック
reachableto = [False for _ in range(N+1)] #終点N-1から始点0へ戻れるかチェック
OK = [False for _ in range(N+1)] #どちらからもいける点を検出。ここ以外の点はどうでもよい。
for i in range(M):
  a,b,c = map(int,input().split())
  a-=1;b-=1 #頂点番号を0スタートに
  c-=P #ここで先に最後に払う分を引いておく。
  c = -c #最短経路にしたいのでコストを負にする。
  edge.append((a,b,c))
  to[a].append(b)
  rto[b].append(a)

def dfs(v):
  if reachablefrom[v]:
    return
  reachablefrom[v] = True
  for u in to[v]:
    dfs(u)

def rdfs(v):
  if reachableto[v]:
    return
  reachableto[v] = True
  for u in rto[v]:
    rdfs(u)
    
dfs(0)
rdfs(N)
for i in range(len(OK)): #len(OK)でもまあ良いか。
  OK[i] = reachablefrom[i]&reachableto[i]
#ここからベルマンフォード法
d = [INF for _ in range(N+1)]
d[0] = 0 #スタートのコストは0
upd = True #サイクルで更新の有無をチェック
step = 0
while upd:
  upd = False
  for i in range(M):
    a,b,c = edge[i]
    if not OK[a] or not OK[b]:
      continue
    new = d[a]+c
    if new < d[b]: #aから来たほうが最短
      upd = True
      d[b] = new
  step += 1
  if step > N+10: #最短経路が頂点の数よりも大きくなることない。
    print("-1")
    sys.exit()
ans = -d[N] #最後、コストをマイナスで戻す
ans = max(0,ans)
print(ans)