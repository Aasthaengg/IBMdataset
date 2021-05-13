import sys
x=y=1
while True:
	x,y=map(int,input().split())
	if x==0: break
	for i in range (1,x+1):
		for j in range (1,y+1):
			sys.stdout.write('#')
		print('')
	print('')