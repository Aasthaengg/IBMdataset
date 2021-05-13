X,Y = map(int,input().split())

X0 = X
res = -1
if X % Y != 0:
	while True:
		if X % Y != 0:
			res = X
			break
		X *= X0

print(res)