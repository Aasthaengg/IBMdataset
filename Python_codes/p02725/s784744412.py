# C - Traveling Salesman around Lake
K, N = map(int, input().split())
A = list(map(int, input().split()))

dist = []
for i in range(N-1):
    dist.append(abs(A[i] - A[i+1]))
dist.append(abs(K - A[-1] + A[0]))
dist = sorted(dist, reverse=True)
print(sum(dist[1:]))