#ABC132-E Hopscotch Addict
"""
グラフを3倍して、
ある二頂点u→vに辺が存在する時
余り0の頂点u→1の頂点v
余り1の頂点u→2の頂点v
余り2の頂点u→0の頂点v
にそれぞれ辺を張った時に、
スタート(頂点S)の余り0の頂点から、
ゴール(頂点T)の余り0への最短パスが答え。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m = map(int,readline().split())
g = [[] for _ in range(3*n)]
for i in range(m):
    x,y = map(int,readline().split())
    x,y = x-1,y-1
    g[x].append([1,y+n])
    g[x+n].append([1,y+n+n])
    g[x+n+n].append([1,y])


#ダイクストラ法通常版
#O(ElogV)
import heapq
def dijkstra_heap(s,edge):
    #始点sから各頂点への最短距離
    n = len(edge)
    d = [float("inf")] * n
    used = [True] * n #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist,e)
    while len(edgelist): #キューから値が無くなるまで
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge[1]]: #既に最小距離が確定しているなら
            continue
        v = minedge[1] #vに頂点を代入
        d[v] = minedge[0] #その頂点のコストに重みを代入
        used[v] = False #vには最小距離が入っていることが証明できる(ヒープキューを使用しているため)
        for e in edge[v]: #頂点vから伸びている辺の先をヒープキューに入れてく
            if used[e[1]]:
                heapq.heappush(edgelist,[e[0]+d[v],e[1]])
    return d #回しきったらreturn(たどり着けなかった頂点はinf.)

s,t = map(int,readline().split())
s,t = s-1,t-1

res = dijkstra_heap(s,g)[t]

print(-1 if res == float("inf") else res//3)