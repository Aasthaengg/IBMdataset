x = list(map(int, input().split()))

cnt = 0
for xx in x:
	cnt += 1
	if xx == 0:
		print(cnt)