s=input()
a = ''
b = ''
c = 0

for i in s:
	a += i
	if a == b:
		continue
	c += 1
	b = a
	a = ''
print(c)