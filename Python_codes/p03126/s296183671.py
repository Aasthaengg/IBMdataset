N,M = map(int, input().split())

B = [0]*30

for i in range(N):
	K, *A = map(int, input().split())
	for a in A:
		B[a-1] += 1

print(sum(c == N for c in B))