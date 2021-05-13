s = input()

k = len(s)
win = 0

for i in range(k):
	if s[i] == 'o':
		win += 1

if k < 7:
	print('YES')
elif k >= 8:
	if win + (15 - k) >= 8:
		print('YES')
	else:
		print('NO')