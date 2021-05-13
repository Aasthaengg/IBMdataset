x,y = map(int,input().split())

if x == y:
	print(-1)
	exit()

i =2

if x < y :
	while x*i % y == 0:
		i = i + 1	
	print(x*i)
	
else:
	if x%y==0:
		print(-1)
	else:
		while x*i % y == 0:
			i = i + 1	
		print(x*i)
		



