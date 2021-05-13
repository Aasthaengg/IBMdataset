n = list(str(int(input())))
c = 0

for i in range(3):
	if n[i] == '7':
		print('Yes')
		break
	c += 1
if c == 3:
	print('No')