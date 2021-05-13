from collections import deque
import sys

n, m = list(map(int, input().split()))

edges = [[] for _ in range(n + 1)]

for _ in range(m):
	u, v = list(map(int, input().split()))
	edges[u].append(v)

s, t = list(map(int, input().split()))
visited = [[] for _ in range(n + 1)]

q = deque()
q.append((s, 0))

while q:
	node, cnt = q.popleft()

	if cnt % 3 in visited[node]:
		continue
	
	if node == t and cnt % 3 == 0:
		print(cnt // 3)
		sys.exit()
	
	else:
		visited[node].append(cnt % 3)
		for e in edges[node]:
			q.append((e, cnt + 1))
	
print(-1)
