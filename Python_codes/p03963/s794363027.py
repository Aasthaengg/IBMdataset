a=input().split(" ")
part=0
 
for i in range(int(a[0])):
	if i==0:
		part=int(a[1])
	else:
		part=part*(int(a[1])-1)
 
print(part)

