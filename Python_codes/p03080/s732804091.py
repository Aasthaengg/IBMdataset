if __name__ == '__main__':
	n = int(input())
	s = input()
	r, b = 0, 0

	for c in s:
		if c == 'R':
			r += 1
		else:
			b += 1
	
	if r > b:
		print('Yes')
	else:
		print('No')
