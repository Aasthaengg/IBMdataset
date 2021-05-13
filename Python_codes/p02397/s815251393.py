def main():

	while True:
		numbers = input().split()
		x, y = map(int, numbers)
		
		if x == 0 and y == 0:
			break

		else:
			if x >  y:
				print('{0} {1}'.format(y, x))
			if x <= y:
				print('{0} {1}'.format(x, y))

	    


if __name__=="__main__":
	main()