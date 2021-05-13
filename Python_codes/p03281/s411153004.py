if __name__ == '__main__':
	n = int(input())

	cnt = 0
	ans = 0
	for x in range(1,n+1,2):
		cnt = 0
		for y in range(1,x+1):
			if x % y == 0:
				cnt += 1
		if cnt == 8:
			ans += 1

	print(ans)
