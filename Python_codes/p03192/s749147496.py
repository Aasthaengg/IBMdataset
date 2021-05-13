x=int(input())
y=0
while x>0:
	if x%10==2:
		y=y+1
	x=x//10
print(y)