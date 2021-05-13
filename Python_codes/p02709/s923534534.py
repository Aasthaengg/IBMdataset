if __name__ == '__main__':
	N = int(input())
	Als = [int(a) for a in input().split()]
	lst = []
	for i in range(N):
		lst.append([Als[i],i+1])

	lst.sort(reverse = True)

	DP = [[0] * (N+1) for _ in range(N+1)]

	ans = 0

	for i in range(1,N+1):
		a = lst[i-1][0]
		index = lst[i-1][1]
		vx = DP[i-1][0] + a * abs(index-i)
		vy = DP[0][i-1] + a * abs(index-(N-i+1))
		DP[i][0] = vx
		DP[0][i] = vy
		if ans < vx:
			ans = vx
		if ans < vy:
			ans = vy

	for i in range(1,N+1):
		for j in range(1,N+1):
			if i + j <= N:
				a = lst[i+j-1][0]
				index = lst[i+j-1][1]
				v = max(DP[i-1][j] + a * abs(index-i),DP[i][j-1] + a * abs(index-(N-j+1)))
				DP[i][j] = v
				if ans < v:
					ans = v
			else:
				break

	print(int(ans))