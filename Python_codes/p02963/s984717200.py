S = int(input())

x1,y1 = 0,0
x2 = 10**9
y2 =1
y3,x3 = divmod(-S,x2)
y3 *= -1
for a in [x1,y1,x2,y2,x3,y3]:
	if a == y3:
		print(a)
	else:
		print(a,end=" ")