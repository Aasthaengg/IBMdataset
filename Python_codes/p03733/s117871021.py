n, t = map(int, input().split())
T = list(map(int, input().split()))
ans = t
for a, b in zip(T, T[1:]):
	ans += min(b - a, t)
print(ans)