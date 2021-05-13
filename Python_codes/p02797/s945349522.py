N, K, S = map(int, input().split())

A = [0]*N

for i in range (0, K):
	A[i] = S

if S == 10**9-1:
	for i in range (K, N):
		A[i] = 10**9
else:
	for i in range (K, N):
		A[i] = 10**9-1

print(*A)