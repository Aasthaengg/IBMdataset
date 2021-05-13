R, G, B, n = map(int, input().split())

res = 0
for r in range(n + 1):
	for g in range(n + 1):
		b = n - r * R - g * G
		if b == 0 or (b > 0 and b % B == 0):
			res += 1
print(res)