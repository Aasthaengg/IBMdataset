def resolve():
	n = int(input())
	if n == 0:
		print("0")
		return
	out = ""
	base = 1
	while n != 0:
		if n % (-2) == 0:
			out = "0" + out
		else:
			r = n % (-2)
			if r < 0:
				r = 1
			n -= r
			out = "1" + out
		n /= (-2)


	print(out)
resolve()