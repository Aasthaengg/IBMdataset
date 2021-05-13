N = int(input())

#隣接リスト
ad = {}
for n in range(N):
    ad[n+1]=[]
    
for n in range(N-1):
    a,b,c = list(map(int,input().split()))
    ad[a].append([b,c])
    ad[b].append([a,c])
    
Query = []
Q,K = list(map(int,input().split()))
for q in range(Q):
    x,y = list(map(int,input().split()))
    Query.append([x,y])

# ダイクストラ（優先度キュー）
import heapq
INF = 10 ** 20

color = {}
for n in range(N):
    color[n+1] = -1
    
dist = {}
for n in range(N):
    dist[n+1] = INF

def dijkstra(start, node_num): 
    HP = []
    dist[start] = 0

    heapq.heappush(HP,[start,0])

    while HP:
        u = heapq.heappop(HP)[0]

        color[u] = 1

        for to, cost in ad[u]:
            if color[to] == -1 and dist[u] + cost < dist[to]:
                dist[to] = dist[u] + cost
                heapq.heappush(HP, (to, dist[to]))
    return dist

start = K
node_num = N
dist = dijkstra(start, node_num)

for x,y in Query:
    print(dist[x]+dist[y])
