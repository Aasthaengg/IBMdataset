a, b, k = map(int, input().split())

cond = 1
for i in range(k):
	if cond == 1:
		if a % 2 == 1:
			a -= 1
		a //= 2
		b += a
		cond = 0
	else:
		if b % 2 == 1:
			b -= 1
		b //= 2
		a += b
		cond = 1

print(a, end = " ")
print(b)