if __name__ == "__main__":
	num = []
	cou = 0
	while True:
		a = input()
		if a == '0':
			break
		num.append(a)
	for i in num:
		cou += 1
		print("Case %d: %s"%(cou,i))