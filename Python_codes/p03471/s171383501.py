N,Y = map(int,input().split())
for i in range(N + 1):
	a = i
	for j in range(N - a + 1):
		b = j
		c = N - a - b
		if a*10000 + b*5000 + c*1000 == Y:
			break
	if a*10000 + b*5000 + c*1000 == Y:
			print(str(a)+" "+str(b)+" "+str(c))
			break
if a*10000 + b*5000 + c*1000 != Y:
	print(str(-1)+" "+str(-1)+" "+str(-1))