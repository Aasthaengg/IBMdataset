x, y, z = map(int, input().split())
i = x
n = 0
while i <= y:
	if z % i == 0:
		n += 1
	i += 1
print(n)