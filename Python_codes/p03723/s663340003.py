def exchg(a, b, c):
	count = 0
	if (a == b == c) and ((a & 1) == 0 and (b & 1) == 0 and (c & 1) == 0):
		return -1
	while((a & 1) == 0 and (b & 1) == 0 and (c & 1) == 0):
		a, b, c = (a+b)//2, (b+c)//2, (c+a)//2
		# print(a, b, c)
		count += 1
	return count
a, b, c = map(int, input().split())
print(exchg(a, b, c))