a,b = (int(i) for i in input().split())
print(100,100)
x,y = a-1,b-1
for i in range(50):
	if i%2==0:
		if x>=50:
			print("#."*50)
			x -= 50
		else:
			print("#."*x+"#"*(100-2*x))
			x = 0
	else: print("#"*100)
for i in range(50):
	if i%2==1:
		if y>=50:
			print(".#"*50)
			y -= 50
		else:
			print(".#"*y+"."*(100-2*y))
			y = 0
	else: print("."*100)