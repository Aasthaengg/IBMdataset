import collections
n = int(raw_input())
adj = collections.defaultdict(list)
for _ in range(n-1):
	u,v = map(int, raw_input().split())
	adj[u].append(v)
	adj[v].append(u)
def bfs(source, adj):
	q = collections.deque([(source,0)])
	distance = {}
	vis = set([source])
	while(q):
		u,d = q.popleft()
		distance[u] = d
		for v in adj[u]:
			if v not in vis:
				vis.add(v)
				q.append((v,d+1))
	return distance
a,b = bfs(1, adj), bfs(n, adj)
print 'Fennec' if 2* sum([+1 if a[u] <= b[u] else 0 for u in range(1, n+1)]) > n else 'Snuke'