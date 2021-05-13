import collections
import heapq
import copy
n,m,p = map(int,raw_input().split(' '))

adj = collections.defaultdict(list)
def f(e,p):
	u,v,w = e
	return (u,v,p-w)

edges = [f(map(int, raw_input().split()), p) for _ in range(m) ]

fa = collections.defaultdict(list)
ba = collections.defaultdict(list)
for u,v,_ in edges:
	fa[u].append(v)
	ba[v].append(u)
def dfs(u,adj,vis):
	stack = collections.deque([u])
	while(stack):
		uu = stack.pop()
		vis.add(uu)

		for v in adj[uu]:
			if v not in vis:
				vis.add(v)
				stack.append(v)
va = set([1])
dfs(1, fa, va)

vb = set([n])
dfs(n, ba, vb)

h = {u: (+float('inf') if u > 1 else 0) for u in range(1, n + 1)}

for _ in range(n-1):
	for u,v,w in edges: h[v] = min(h[v], h[u] + w)

fnc = False
for u,v,w in edges: 
	if v in va and v in vb and h[v] > h[u] + w:
		fnc = True
		break
print max(0,-h[n]) if (not(fnc) and h[n] != +float('inf')) else -1 