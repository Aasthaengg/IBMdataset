import sys
while True:
	y,x=map(int, input().split())
	if x==y==0: break
	print('#'*x)
	for i in range(2,y)	:
		sys.stdout.write('#')
		sys.stdout.write('.'*(x-2))
		print('#')
	print('#'*x+'\n')