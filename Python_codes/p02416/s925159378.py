while True:
	strnum = raw_input().strip()
	if strnum == "0":
		break
	else:
		wa = 0
		for c in strnum:
			wa += int(c)
		print wa