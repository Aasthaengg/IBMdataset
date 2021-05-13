n = int(input())
f = True
for i in range(n):
	a = int(input())
	if a % 2 != 0:
		f = False
print('second' if f else 'first')