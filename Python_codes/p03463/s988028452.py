N,A,B = map(int,input().split(' '))

k = abs(A-B)

if k % 2 == 0:
	print("Alice")
else:
	print("Borys")
