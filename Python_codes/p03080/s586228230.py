n = int(input())
s = input()

r = 0
b = 0

for i in range(n):
	if s[i] == 'R':
		r += 1
	elif s[i] == 'B':
		b += 1

if r > b:
	print('Yes')
else:
	print('No')