while True:
	try:
		list = [int(item) for item in raw_input().split()]
		list.sort()
		if list[0] ** 2 + list[1] ** 2 == list[2] ** 2 :
			print 'YES'
		else :
			print 'NO'
	except EOFError:
		break
	except IndexError:
		continue