a,b,k=map(int,input().split())
def co(x, y):
	x //= 2
	y += x
	return x, y

for i in range(k):
	if i % 2 == 0:
		a,b = co(a,b)
	else:
		b,a = co(b,a)
print(a,b)