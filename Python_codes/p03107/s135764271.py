s = input()
a = 0
b = 0
for c in s:
	if c == '0':
		a += 1
	else:
		b += 1
print(min(a, b) * 2)