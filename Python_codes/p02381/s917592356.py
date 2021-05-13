while True:
	n = int(raw_input())
	if n == 0:
		break
	else:
		data = map(int, raw_input().split())

		all_sum = 0
		for i in range(n):
			all_sum += data[i]
		ave = all_sum * 1.0 / n

		bunsan_sum = 0
		for i in range(n):
			bunsan_sum += (data[i] - ave)**2
		bunsan = bunsan_sum / n

		alpha = bunsan ** 0.5

		print("{:.8f}".format(alpha))