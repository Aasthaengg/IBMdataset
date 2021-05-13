y,x = sorted([int(s) for s in input().split()])

while y:
	x,y = y,x%y
print(x)