a = list(map(int, input().split()))
count = 0
while all(x % 2 == 0 for x in a) and count <= 100000:
	b = [(sum(a) - x) // 2 for x in a]
	a = b
	count += 1
print(count if count <= 100000 else -1)