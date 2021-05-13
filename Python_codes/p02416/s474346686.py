while True:

	num = input()
	if num == "0":
		break
	else:
		k = 0
		for j in num:
			k += int(j)
		print(k)

