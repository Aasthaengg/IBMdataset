while True:
	data = input()
	if data == '0':
		break
	else:
		data = [int(s) for s in data]
		print(sum(data))