N, A, B = map(int, input().split())
X = list(map(int, input().split()))
dist = []
ans = 0

for i in range(N - 1):
	dist.append(X[i + 1] - X[i])
	
for i in range(N - 1):
	ans += min(dist[i] * A, B)
	
print(ans)