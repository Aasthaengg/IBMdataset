n=input()
a=[]
area=[]
x1=[]
x2=[]

x=1
for i in n:
	if i=='\\':
		a.append(x)
		
	elif i=='/' and len(a)>=1:
		area.append(x-a[len(a)-1])
		x1.append(a[len(a)-1])
		x2.append(x)
		a.pop()		
		
		for i in range(len(x1)-2,-1,-1):	
			if x1[len(x1)-1]<x1[i] and x2[len(x2)-1]>x2[i]:
				x1.pop(i)
				x2.pop(i)
				area[i]=area[i]+area[len(area)-1]
				area.pop()
	x+=1

print(sum(area))
print(len(area),*area)

	

