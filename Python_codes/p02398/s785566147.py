if __name__ == "__main__":
	cou = 0
	a, b, c = map( int, input().split() )
	for i in range(a,b+1):
		if c % i == 0:
			cou += 1
	print(cou)