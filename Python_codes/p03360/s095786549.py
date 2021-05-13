def resolve():
	nums = list(map(int, input().split()))
	k = int(input())
	ans = 0
	for i in range(k):
		m = 0
		for j in range(1, 3):
			if nums[m] < nums[j]:
				m = j
		nums[m] *= 2
	print(sum(nums))
resolve()