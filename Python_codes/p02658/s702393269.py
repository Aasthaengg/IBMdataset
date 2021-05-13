if __name__ == '__main__':

	INF = 10**18
	
	n = int(input())
	A = list(map(int,input().split()))

	if 0 in A:
		print(0)
		exit()

	ans = 1
	flg = False

	for i in range(n):
		ans = ans * A[i]
		if ans > INF:
			ans = -1
			break

	print(ans)
