str = ''
while True:
	try:
		a = input().lower()
		str = str + a
	except EOFError:
		break

for i in 'abcdefghijklmnopqrstuvwxyz':
	print('{0} : {1}'.format(i, str.count(i)))