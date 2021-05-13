def gcd(x, y):
	if x < y:
		tmp = y
		y = x
		x = tmp
	
	if x % y == 0:
		return y
	else:
		return gcd(y, x % y)


#input number
l = raw_input()

x, y = [int(e) for e in l.split()]
 
if x < 1 and x > 10000000000:
	exit()

if y < 1 and y > 10000000000:
	exit()

print gcd(x, y)