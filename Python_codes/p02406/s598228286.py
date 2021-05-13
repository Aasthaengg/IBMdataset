x = input()
y= []
for i in range(x+1):
	if i == 0:
		continue
	if i % 3 == 0:
		y.append(str(i))
	else:
		z = i
		while 1:
			if z % 10 == 3:
				y.append(str(i))
				break
			z /= 10
			if z == 0:
				break
print " " + " ".join(y)