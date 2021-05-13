AB = [list(map(int, input().split())) for _ in range(3)]

g = [[] for _ in range(4)]
for a, b in AB:
	a, b = a - 1, b - 1
	g[a] += [b]
	g[b] += [a]

def dfs(v, p, visited=None):
	if None == visited:
		visited = [False] * 4
	visited[v] = True
	for n in g[v]:
		if visited[n]:
			continue
		if n == p:
			continue
		return dfs(n, v, visited)
	return all(visited)

#print([dfs(x, -1) for x in range(4)])
print(["YES", "NO"][not(any([dfs(x, -1) for x in range(4)]))])
