K, N = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 10 ** 6
for i in range(N):
	if i > 0:
		x = K - A[i] + A[i - 1]
	else:
		x = A[i - 1] - A[i]
	ans = min(ans, x)
print(ans)

