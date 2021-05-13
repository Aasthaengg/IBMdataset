c=w=0
for i in input():
	if i=="g":
		if c:
			w+=1
			c-=1
		else:
			c+=1
	else:
		if c:
			c-=1
		else:
			c+=1
			w-=1
print(w)