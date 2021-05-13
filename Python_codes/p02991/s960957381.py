from collections import deque
import sys

n, m = list(map(int, input().split()))

edges = [[[] for _ in range(3)] for _ in range(n + 1)]

for _ in range(m):
	u, v = list(map(int, input().split()))
	edges[u][0].append((v, 1))
	edges[u][1].append((v, 2))
	edges[u][2].append((v, 0))

s, t = list(map(int, input().split()))
visited = [[[] for _ in range(3)] for _ in range(n + 1)]

q = deque()
q.append((s, 0, 0))

while q:
	node, div, cnt = q.popleft()

	if visited[node][div] == 1:
		continue
	
	if (node, div) == (t, 0):
		print(cnt // 3)
		sys.exit()
	
	else:
		visited[node][div] = 1
		for e in edges[node][div]:
			q.append((e[0], e[1], cnt + 1))
	
print(-1)
