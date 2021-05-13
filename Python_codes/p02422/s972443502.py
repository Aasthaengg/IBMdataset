str = raw_input()
q = int(raw_input())

for i in range(q):
	do_list = raw_input().split()
	a = int(do_list[1])
	b = int(do_list[2])
	if do_list[0] == "print":
		print(str[a:(b+1)])
	elif do_list[0] == "reverse":
		part = str[a:(b+1)]
		rev = ""
		for j in range(len(part)):
			rev += part[-j-1]
		if a == 0:
			str = rev + str[(b+1):]
		elif b == len(str)-1:
			str = str[:a] + rev
		else:
			str = str[:a] + rev + str[(b+1):]
	else:
		p = do_list[3]
		if a == 0:
			str = p + str[(b+1):]
		elif b == len(str)-1:
			str = str[:a] + p
		else:
			str = str[:a] + p + str[(b+1):]