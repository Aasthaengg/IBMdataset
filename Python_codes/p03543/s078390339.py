n = int(input())
n = list(str(n))
c = 0
for i in range(2):
	if n[i] == n[i+1] == n[i+2]:
		c += 1
if c >= 1:
	print('Yes')
else:
	print('No')