
import sys
def input():
	return sys.stdin.readline().strip()


N, M = list(map(int, input().split()))

edge_list = []
for _ in range(M):
	a, b, c = list(map(int, input().split()))
	a -= 1
	b -= 1
	edge_list.append((a, b, c))
dist = [-(10**20) for _ in range(N)]
dist[0] = 0

for times in range(N):
	for edge in edge_list:
		if dist[edge[0]] > -(10**20):
			if dist[edge[1]] == -(10**20):
				dist[edge[1]] = dist[edge[0]] + edge[2]
			else:
				dist[edge[1]] = max(dist[edge[1]], dist[edge[0]] + edge[2])
score = dist[N - 1]

for times in range(N):
	for edge in edge_list:
		if dist[edge[0]] > -(10**20):
			if dist[edge[1]] == -(10**20):
				dist[edge[1]] = dist[edge[0]] + edge[2]
			else:
				dist[edge[1]] = max(dist[edge[1]], dist[edge[0]] + edge[2])

if score < dist[N - 1]:
	print("inf")
else:
	print(dist[N - 1])