a, b, k = map(int, input().split())

for i in range(1,k+1):
	
	if i % 2 == 0:
		if b % 2 != 0:
			b -= 1
		c = int(b/2)
		b -= c
		a += c
	else:
		if a % 2 != 0:
			a -= 1
		c = int(a/2)
		a -= c
		b += c

print(str(a) + " " + str(b))
