##########################################
inf=10**9
import heapq
class Dijkstra():
    """
    ・有向 / 無向は問わない(無向の場合は，逆向きの辺もたす)
    ・負のコストがない場合のみ
    ・計算量はO(E log|V|)　
    ・heapを使うことで頂点を走査する必要がなくなる（代わりに，距離更新したものは確定でなくともqueに入れておく）
    """    
    class Edge():
        #重み付き有向辺
        
        def __init__(self, _to, _cost):
            self.to =_to
            self.cost = _cost
    
    def __init__(self, V):
        #引数Vは頂点数
        self.G = [[] for _ in range(V)] #隣接リストG[u][i]が頂点uのi番目の辺
        self. _E = 0 #辺の数
        self._V = V #頂点数
    
    #proparty - 辺の数
    def E(self):
        return self._E
    
    #proparty - 頂点数
    def V(self):
        return self._V
    
    def add(self, _from, _to, _cost):
        #2頂点と辺のコストを追加
        self.G[_from].append(self.Edge(_to,_cost))
        self._E +=1
        
    def add2(self, _from, _to, _cost):
        #2頂点と辺のコスト（無向）を追加
        self.G[_from].append(self.Edge(_to, _cost))
        self.G[_to].append(self.Edge(_from, _cost))
        self._E +=1
        
    def shortest_path(self,s):
        #始点sから頂点iまでの最短経路長のリストを返す
        
        que = [] #priority queue
        d = [inf] * self.V()
        prev = [None]*self.V() #prev[j]は，sからjへ最短経路で行くときのjの一つ前の場所
        d[s] = 0
        heapq.heappush(que,(0,s)) #始点の距離と頂点番号をヒープに追加
        
        while len(que)!=0:
            #キューに格納されてある中で一番コストが小さい頂点を取り出す
            cost,v = heapq.heappop(que)
            
            #キューに格納された最短経路長候補がdの距離よりも大きい場合に処理をスキップ
            if d[v] < cost:
                continue
                
            #頂点vに隣接する各頂点iに対して，vを経由した場合の距離を計算して，これがd[i]よりも小さい場合に更新
            for i in range(len(self.G[v])):
                e = self.G[v][i] #vのi個目の隣接辺
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost #更新
                    prev[e.to] = v
                    heapq.heappush(que,(d[e.to],e.to)) #queに新たな最短経路長候補を追加

        return d
########################

#グラフの頂点を3倍化

import sys
input = sys.stdin.readline

N,M=map(int,input().split())
djk = Dijkstra(N*3)

for i in range(M):
    u,v=map(int,input().split())
    u-=1
    v-=1
    djk.add(u,N+v,1)
    djk.add(N+u,2*N+v,1)
    djk.add(2*N+u,v,1)
S,T=map(int,input().split())

d = djk.shortest_path(S-1)
ans=d[T-1]//3
if ans==inf//3:
    ans=-1
print(ans)