while True:
	numbers = map(int, raw_input().split())
	max_ = numbers[0]
	goal = numbers[1]
	cnt = 0
	if max_ == 0 and goal == 0:
		break
	else:
		i = max_
		while 3 * i - 3 >= goal:
			j = i-1
			while goal - i - j < j:
				if goal - i - j > 0:
					cnt += 1
				j -= 1
			i -= 1
	print cnt