s = input()
cnt, res = 0, 0
for i in s:
	if i in 'ATGC':
		cnt += 1
		res = max(cnt, res)
	else:
		cnt = 0
print(res)