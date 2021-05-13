from collections import defaultdict
import queue

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

s, t = map(int, input().split())

graph = defaultdict(list)

for edge in edges:
	u, v = edge
	graph[u].append(v + n)
	graph[u + n].append(v + 2*n)
	graph[u + 2*n].append(v)

def bfs(s, t, graph):
	vis_set = set()
	dist = defaultdict(lambda: int(-1))
	dist[s] = 0
	que = queue.Queue()
	que.put(s)
	vis_set.add(s)	

	while not que.empty():
		vert = que.get()
		for nxt in graph[vert]:
			if nxt not in vis_set:
				dist[nxt] = dist[vert] + 1
				vis_set.add(nxt)
				que.put(nxt)
				if nxt == t:
					return dist[nxt]//3
	return -1
ans = bfs(s, t, graph)
print(ans)