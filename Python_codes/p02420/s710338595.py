while True:
	string = input()
	if string == '-':
		break
	# ??????????????°
	for i in range(int(input())):
		num = int(input())
		string = string[num:] + string[:num]
	print(string)