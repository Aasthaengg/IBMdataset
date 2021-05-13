n = int(input())
s = [input() for i in range(n)]
 
ab = 0
a = 0
b = 0
 
d = 0
for i in s:
	d += i.count('AB')
	if i[0] == 'B' and i[-1] == 'A':
		ab += 1
	elif i[-1] == 'A':
		a += 1
	elif i[0] == 'B':
		b += 1
 
if ab == 0:
	d += min(a,b)
elif a+b == 0:
	d += ab-1
else:
	d += ab+min(a,b)
print (d)