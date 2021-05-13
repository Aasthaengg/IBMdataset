r, g, b, n = map(int, input().split())
count = 0
for x in range(n//r + 1):
	for y in range((n - r*x)//g + 1):
		if (n - (r*x + g*y)) % b == 0:
			count += 1
print(count)