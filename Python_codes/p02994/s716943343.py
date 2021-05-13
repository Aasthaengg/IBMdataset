N, L = list(map(int, input().split()))
ans = 0
l = N + abs(L)
for i in range(N):
	a = L + i
	if abs(a) < abs(l):
		l = a
	ans += a

print(ans - l)
