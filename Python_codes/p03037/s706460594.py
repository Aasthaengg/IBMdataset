N, M = list(map(int, input().split()))
L, R = 0, N + 1
for i in range(M):
	l, r = list(map(int, input().split()))
	L = max(L, l)
	R = min(R, r)
print(max(R - L + 1, 0))
