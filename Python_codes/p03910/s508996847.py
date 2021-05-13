n = int(input())

cnt = 0
for i in range(1, n + 1):
	cnt += i
	if cnt >= n:
		res = i
		break
	
remove = cnt - n
for i in range(1, res + 1):
	if i != remove:
		print(i)