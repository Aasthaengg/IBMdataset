import math
s = input().split()
a = int(s[0])
b = int(s[1])
k = int(s[2])
for i in range(k):
	if(i % 2 == 0):
		b += int(math.floor(a / 2))
		a = int(math.floor(a / 2))
	else:
		a += int(math.floor(b / 2))
		b = int(math.floor(b / 2))
print("{0} {1}".format(a,b))