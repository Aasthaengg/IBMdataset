if __name__ == "__main__":
	list = {}
	i = 0
	while True:
		a,op,b = input().split()
		a,b = map(int,[a,b])
		if op == '+':
			list[i] = a+b
		elif op == '-':
			list[i] = a - b
		elif op == '*':
			list[i] = a*b
		elif op == '/':
			c = a/b
			list[i] = int(c)
		else:
			break
		i +=1
	for i in range(len(list)):
		print (list[i])