from collections import deque

def solve(N, M, graph):

	indegree = {n: 0 for n in range(1, N + 1)}
	for node in graph:
		for nei in graph[node]:
			indegree[nei] += 1

	queue = deque()
	for node in graph:
		if indegree[node] == 0:
			queue.append(node)

	lengths = [0] * (N + 1)

	while queue:
		node = queue.popleft()

		for nei in graph[node]:
			indegree[nei] -= 1

			if indegree[nei] == 0:
				queue.append(nei)

			lengths[nei] = max(lengths[nei], lengths[node] + 1)

	return max(lengths)


N, M = [int(s) for s in input().split()]
graph = {}
for n in range(1, N + 1):
	graph[n] = []
for _ in range(M):
	x, y = [int(s) for s in input().split()]
	graph[x].append(y)

print(solve(N, M, graph))