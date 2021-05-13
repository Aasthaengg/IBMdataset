#ABC137-E Coins Respawn
"""
1の移動に対してpだけコストを支払うと考える事ができる。
pを考慮しても無限にコインを増やすような閉路が存在する場合、-1を出力、そうでないならばコストが最大と
なるようにゴールに行くことが最適である。
すべての辺上のコインをマイナス値でもって、pを足し合わせることによってこれが達成できる。
ベルマンフォード法を用いて負の重みを扱えるようにする。
この時、負の閉路の検出が可能だが、この問題では1→Nへの道とは関係ない場所に負の閉路が存在しても、
それは無限にコインを増やせるとは言わない。
よって、まず1と関係する辺をすべて求めた後、Nと関係する逆辺を求める事により、どちらもに該当しない辺を除去することで達成できる。
"""
import sys
from collections import deque
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m,p = map(int,readline().split())
g = [[] for i in range(n)]
rev = [[] for i in range(n)] #逆辺
for i in range(m):
	x,y,w = map(int,readline().split())
	x,y,w = x-1,y-1,-w
	g[x].append((y,w+p))
	rev[y].append((x,w+p))

res1 = [0]
queue = deque([0])
#頂点1からスタートして、関係のある辺を求める
while True:
	if len(queue) <= 0:
		break
	v = queue.pop()
	for e in g[v]:
		if e[0] not in res1:
			res1.append(e[0])
			queue.append(e[0])
		else:
			continue

res2 = [n-1]
queue = deque([n-1])
#頂点nからスタートして、関係のある辺を求める
while True:
	if len(queue) <= 0:
		break
	v = queue.pop()
	for e in rev[v]:
		if e[0] not in res2:
			res2.append(e[0])
			queue.append(e[0])
		else:
			continue
itr = set([i for i in range(n)])
res3 = itr - (set(res1) & set(res2))

def BellmanFord(edges,num_v,source): #[x,y,weight]のリスト,頂点数,始点
	#グラフの初期化
	inf=float("inf")
	dist=[inf for i in range(num_v)]
	dist[source]=0
	#辺の緩和
	for i in range(num_v):
		for edge in edges:
			if edge[0] != inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
				dist[edge[1]] = dist[edge[0]] + edge[2]
				if i==num_v-1: return [] #負の閉路が存在する場合,空のリストが帰る
  
	return dist

edges = []
for i in range(n):
	if i in res3:
		continue
	for j in g[i]:
		if j[0] in res3:
			continue
		edges.append([i,j[0],j[1]])

dist = BellmanFord(edges,n,0)

if len(dist) == 0:
	print(-1)
else:
	print(max(0,-dist[n-1]))