def my_func(i):
	return i*i
raw_input()
while True:
	try:
		splited = map(int, raw_input().split())
		sort_num = sorted(splited)
		if my_func(sort_num[0])+my_func(sort_num[1]) == my_func(sort_num[2]):
			print 'YES'
		else:
			print 'NO'
	except EOFError:
		break