if __name__ == '__main__':
	a, b, c = list(map(int, input().split(' ')))
	if a == b and b == c:
		print('Yes')
	else:
		print('No')
