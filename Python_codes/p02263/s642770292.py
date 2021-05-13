def kei(a,i,x,y):
	if a[i]=="+":
		st=x+y
		#print("+")
	elif a[i]=="-":
		st=y-x
		#print("-")
	elif a[i]=="*":
		st=x*y
		#print("*") 
	return st


a=[]
stac=[]
a=list(input().split())
for i in range(len(a)):
	if a[i].isdigit():
		stac.append(int(a[i]))
		#print(stac)
	else:
		x=stac.pop()
		y=stac.pop()
		stac.append(kei(a,i,x,y))
		
print(stac[0])
		

