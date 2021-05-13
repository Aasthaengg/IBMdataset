A, B, K = list(map(int, input().split()))
a = A
b = B
for i in range(K):
	if i % 2 == 0:
		if a % 2 == 1:
			a -= 1
		b += int(a // 2)
		a = int(a // 2)
	else:
		if b % 2 == 1:
			b -= 1
		a += int(b // 2)
		b = int(b // 2)

print(a, b)