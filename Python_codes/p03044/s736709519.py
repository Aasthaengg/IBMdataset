import collections
n = int(raw_input())

adj = collections.defaultdict(list)

for _ in range(n - 1):
	u, v, w = map(int, raw_input().split(' '))
	adj[u].append((v,w))
	adj[v].append((u,w))


q = collections.deque([(1,0)])
h = { 1:0 }
while(q):
	u,c = q.popleft()
	for v,w in adj[u]:
		if v not in h:
			h[v] = (1- c) if (w % 2) else c
			q.append((v,h[v]))

for node in range(1, n + 1): 
	print h[node]