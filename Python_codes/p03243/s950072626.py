if __name__ == '__main__':
	
	n = int(input())


	for i in range(n,1000):
		tmp = set(str(i))

		if len(tmp) == 1:
			print(i)
			break
