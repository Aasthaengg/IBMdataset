def resolve():
	s = input().split()
	uni = []
	for i in s:
		if i not in uni:
			uni.append(i)
	print(len(uni))
resolve()