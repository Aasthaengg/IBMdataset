n = input()
if int(n) < 10:
	print(int(n))
	exit()
flag = n[1:] != '9' * (len(n) - 1)
print(int(n[0]) - flag + 9*(len(n) - 1))