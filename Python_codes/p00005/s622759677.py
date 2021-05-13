while True:
	try:
		while True:
			ints = raw_input()
			if ints != '':
				x = map(int,ints.split(' '))
				x.sort()
				a = x[1]
				b = x[0]
				while True:
					m=a%b
					if m!=0:
						a=b
						b=m
						continue
					else:
						break
				n = x[1]*x[0]/b
				print b,n
				continue
			else:
				break
	except: break