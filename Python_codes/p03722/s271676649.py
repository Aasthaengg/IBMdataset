N,M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    E[a-1].append((b-1, -c))
    
    
#ベルマンフォード法:負閉路の検出とある一点から他のすべての点への最短距離の算出

def BellmanFord(E, N, source):
    #E:E[a]は頂点aを始点とする辺のリストであり、辺の終点bと辺の重みwが(b, w)の形で格納されている
    #N:頂点の数
    #source:始点
    #グラフの初期化
    inf = 10**20
    d = [inf for _ in range(N)]
    d[source] = 0
    
    #辺の緩和
    for i in range(N):
        for j in range(N):
            e = E[j]
            if len(e) == 0:
                continue
            for edge in e:
                if d[edge[0]] > d[j] + edge[1]:
                    d[edge[0]] = d[j] + edge[1]
                    if i == N-1 and edge[0] == N-1:
                        return -1
    
    return d

dist = BellmanFord(E, N, 0)
if dist == -1:
    print("inf")
else:
    print(-dist[N-1])