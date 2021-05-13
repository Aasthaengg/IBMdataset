# li = list(map(int, input().split()))
s = input()
n = len(s)
a = n; b = -1;
for i in range(n):
	if s[i] == 'C':
		a = i
		break
for i in range(n-1, -1, -1):
	if s[i] == 'F':
		b = i
		break
if b < a:
	print('No')
else:
	print("Yes")