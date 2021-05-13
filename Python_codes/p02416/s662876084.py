while True:
	ipt=raw_input()
	if ipt=="0":
		break
	k=0
	for i in ipt:
		k+=int(i)
	print k