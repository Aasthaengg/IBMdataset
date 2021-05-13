while True:
	num = list(map(int,*input().split()))
	if num == [0]:
		break
	print(sum(num))