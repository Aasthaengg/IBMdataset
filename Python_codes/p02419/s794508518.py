
while True :
	count_1 = 0
	w = raw_input()
	while True :
		t = raw_input()
		if t=='END_OF_TEXT':
			break
		else :
			a_list = t.lower().split()
	 		for i in a_list:
				if (w==i):
					count_1 += 1
	print(count_1)
	if t=='END_OF_TEXT':
		break