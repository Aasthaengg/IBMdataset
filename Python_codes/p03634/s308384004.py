n = int(raw_input())
import collections
adj = collections.defaultdict(list)
for _ in range(n-1):
	u,v,w = map(int,raw_input().split())
	adj[u].append((v,w))
	adj[v].append((u,w))

dist =  {}
qq,k = map(int, raw_input().split())
vis = set([])
q = collections.deque([(k,0)])
while(q):
	u, c = q.popleft()
	dist[u]  = c
	for v,w in adj[u]:
		if v not in vis: 
			vis.add(v)
			q.append((v,w+c))
for _ in range(qq):
	u,v = map(int, raw_input().split())
	print dist[u] + dist[v]
