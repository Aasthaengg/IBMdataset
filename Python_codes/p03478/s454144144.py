n, a, b = map(int, input().split())
ans = 0
for i in range(n+1):
	sum_ = 0
	m = i

	while True:
		sum_ += m % 10
		m //= 10
		if not m:
			break
	if a <= sum_ <= b:
		ans += i

print(ans)