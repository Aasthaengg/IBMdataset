while True:
	string = input()
	if string == '-':
		break
	n = int(input())
	for i in range(n):
		x = int(input())
		tmp = string[0:x]
		string = string[x:]
		string+=tmp
	print(string)