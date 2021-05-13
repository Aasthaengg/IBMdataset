def call(n):
	i = 1
	while True:
		through_flag = False
		x = i
		if x % 3 == 0:
			print(" {}".format(i), end="")
			through_flag = True
		if not through_flag:
			while True:
				if x % 10 == 3:
					print(" {}".format(i), end="")
					through_flag = True
				if not through_flag:
					x //= 10
					if x == 0: break
				if through_flag: break
		i += 1
		if i > n: break
	print("")



call(int(input()))