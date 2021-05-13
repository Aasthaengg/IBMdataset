def collatz(n):
	c = 1
	check = [n]
	while(True):
		c += 1
		if n & 1 == 0:
			n = n // 2
			if n in check:
				break
			check.append(n)
		else:
			n = (n * 3) + 1
			if n in check:
				break
			check.append(n)
	return c
n = int(input())
print(collatz(n))