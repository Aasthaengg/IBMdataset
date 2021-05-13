def candy(arr, n, x):
	if sum(arr) == x:
		return n
	arr.sort()
	best = 0
	j = 0
	while(j < n):
		temp = x
		c = 0
		for i in range(j, n-1):
			if arr[i] < temp:
				c += 1
				temp -= arr[i]
			elif arr[i] == temp:
				c += 1
				break
			if i == n - 2:
				if temp == arr[n-1]:
					c += 1
		best = max(best, c)
		j += 1
	return best
n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(candy(arr, n, x))