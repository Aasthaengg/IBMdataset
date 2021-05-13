import collections
n = int(raw_input())
adj = collections.defaultdict(list)
for _ in range(n - 1):
	u, v, w = map(int, raw_input().split(' '))
	adj[u].append((v,w))
	adj[v].append((u,w))
h = [-1 for _ in range(n+1)]
h[1] = 0
def dfs(h, adj):
	stack = collections.deque([1])
	while(stack):
		u = stack.pop()
		for v,w in adj[u]:
			if h[v] == -1:
				h[v] = (1- h[u]) if (w % 2) else h[u]
				stack.append(v) #(v, h, adj)
dfs(h, adj)
for node in range(1, n + 1):  print h[node]