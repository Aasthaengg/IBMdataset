n,x,y = map(int,input().split())

import heapq

def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [float('inf')] * n # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost

e = [[] for _ in range(n)]
for i in range(n-1):
    e[i].append((1, i+1))
    e[i+1].append((1, i)) # 有向グラフでは削除
e[x-1].append((1, y-1))
e[y-1].append((1, x-1))

d = [sorted(dijkstra(i)[i:]) for i in range(n)]

import bisect

for i in range(1,n):
    ans = 0
    for j in range(n):
        ans += bisect.bisect_right(d[j], i) - bisect.bisect_left(d[j], i)
    print(ans)