while True:
	mark = map(int, raw_input().split())
	chukan = mark[0]
	kimatu = mark[1]
	saishi = mark[2]
	wa = chukan + kimatu
	if chukan == -1 and kimatu == -1 and saishi == -1:
		break
	elif chukan == -1 or kimatu == -1:
		print("F")
	elif 80 <= wa:
		print("A")
	elif 65 <= wa and wa < 80:
		print("B")
	elif 50 <= wa and wa < 65:
		print("C")
	elif 30 <= wa and wa < 50:
		if 50 <= saishi:
			print("C")
		else:
			print("D")
	else:
		print("F")