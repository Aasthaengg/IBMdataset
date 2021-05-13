if __name__ == '__main__':
	n = int(input())

	cnt = 0
	for x in range(1,n+1):
		s = str(x)
		if len(s) % 2 == 1:
			cnt += 1

	print(cnt)
