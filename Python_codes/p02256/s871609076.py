[x,y] = list(map(int, input().split()))

if x<y:
	temp = x
	x = y
	y = temp

while y>0:
	temp = x % y
	x = y
	y = temp

print(x)