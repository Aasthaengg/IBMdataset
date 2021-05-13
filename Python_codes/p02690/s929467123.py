x=int(input())
for a in range(-200,201):
	f=False
	for b in range(-201,201):
		if a**5-b**5==x:
			print(a,b)
			f=True
			break
	if f:break