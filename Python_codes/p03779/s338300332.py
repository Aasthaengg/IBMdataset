x = int(input())
d = 0
for j in range(10 ** 9):
	d += j
	if d >= x:
		print(j)
		exit()