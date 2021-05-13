x = int(input())
count = 0

if 6 < x <= 11:
	print(2)
elif x <= 6:
	print(1)
else:
	initcount = x // 11
	if initcount:
		count += initcount*2
		x -= initcount * 11
		mod = x % 11
		if 6 < mod <= 11:
			count += 2
		elif 0 < mod <= 6:
			count += 1
		else:
			pass
		print(count)