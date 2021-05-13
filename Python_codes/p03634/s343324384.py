N = int(input())
G = [dict() for i in range(N)]
for i in range(N-1):
    a,b,c = map(int,input().split())
    G[a-1][b-1] = c
    G[b-1][a-1] = c

Q,K = map(int,input().split())

inf = 10**20
import heapq 
# 条件:グラフに負辺がないこと(もちろん負の閉路はない)
# V=ノード数,E=エッジ数とすると、計算量はO((V+E)logV)
# ついでに指定した始点-終点間の最短経路を求められる
def Dijkstra(ad_dict,start): # startから各頂点への最短距離を求める
    distance = [inf for _ in range(N)] # startからの距離
    previous = [inf for _ in range(N)] # previous[i]:頂点iに至る直前に居た頂点の番号．これを持っておけば，goalからstartまで戻れる
    distance[start] = 0
    hq = []
    heapq.heappush(hq, (0, start)) # (startからvへの暫定距離,v)を追加
    while hq:
        temp_dist, prev = heapq.heappop(hq)
        if distance[prev] < temp_dist:
            # startからprevまでの距離がtemp_distより小さいなら，既により最適な経路があるから，この経路は不採用
            continue
        for now, cost in ad_dict[prev].items():
            if (distance[prev] + cost) < distance[now]: # より最適なら更新
                distance[now] = distance[prev] + cost # 最短距離更新
                heapq.heappush(hq, (distance[now], now))
                previous[now] = prev
    return distance, previous # distance:list([int,int,...]), previous:list([int,int,...])

def reconstruct_path(distance, previous, goal): # 最短経路復元
    now = goal
    path = [goal]
    while previous[now] != inf: # now == startのときに停止
        path.append(previous[now])
        now = previous[now]
    return list(path[::-1]) # start -> goalの最短経路

D,_ = Dijkstra(G,K-1)
for i in range(Q):
    x,y = map(int,input().split())
    print(D[x-1]+D[y-1])