
while True:
	a,op,b = raw_input().split()
	if op == '?':
		break
	elif op == '+':
		print int(a) + int(b)
	elif op == '-':
		print int(a) - int(b)
	elif op == '*':
		print int(a) * int(b)
	else:
		print int(a) / int(b)