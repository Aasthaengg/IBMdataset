def resolve():
	n = int(input())
	if n == 0:
		print("0")
		return
	out = []
	while n != 0:
		n, rem = divmod(n, -2)
		if rem < 0:
			n += 1
			rem -= -2
		out.append(rem)
	print("".join(map(str, out[::-1])))
resolve()