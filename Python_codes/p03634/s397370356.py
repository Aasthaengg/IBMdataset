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

n = int(input())
e = [[] for _ in range(n)]
for _ in range(n-1):
	a,b,c = map(int,input().split())
	a,b = a-1, b-1
	e[a].append((c, b))
	e[b].append((c, a))
q,k = map(int,input().split())
l = dijkstra(k-1)
for _ in range(q):
	x,y = map(int,input().split())
	print(l[x-1] + l[y-1])