s = input()
for i in s:
	if i == '1':
		print('9', end="")
	elif i == '9':
		print('1', end="")
	else:
		print(i, end="")