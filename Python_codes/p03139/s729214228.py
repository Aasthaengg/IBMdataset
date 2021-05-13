N,X,Y = map(int, input().split())

if(Y > X):
	b_max = X
	b_min = X + Y - N
else:
	b_max = Y
	b_min = X + Y - N
if(b_min < 0):
	b_min = 0

print(b_max, b_min)