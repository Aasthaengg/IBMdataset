while True:
	try:
		temp = [int(x) for x in raw_input().split()]
		m = max(temp)
		n = min(temp)

		while True:
			if n == 0:
				print m, (temp[0]*temp[1])/m
				break
			else:
				temp2 = n
				n = m % n
				m = temp2

	except:
		break