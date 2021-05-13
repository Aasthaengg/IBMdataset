import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [set() for _ in range(n)]
for _ in range(m):
	a, b = map(int , input().split())
	if (b-1) not in graph[a-1]: graph[a-1].add(b-1)
	if (a-1) not in graph[b-1]: graph[b-1].add(a-1)
clusters = 0
v = [False]*n
for i in range(n):
	if not v[i]:
		v[i] = True
		q = deque([i])
		cluster = 0
		while q:
			node = q.popleft()
			cluster+=1
			for j in graph[node]:
				if not v[j]: v[j] = True; q.append(j)
		clusters = max(clusters, cluster)
print(clusters)

