# n=int(input())
n,k=list(map(int,input().split(" ")))
a=list(map(int,input().split(" ")))
mat=[]
a=list(set(a))
res=["L"]*(k+1)
z=min(a)
for i in range(1,k+1):
	if(i in a):
		# print("lol",i)
		res[i]="W"
	else:
		flag=False
		for j in range(len(a)):
			# print(i,k-a[j],res[k-a[j]])
			# print(a)
			if((i-a[j])>=0 and res[i-a[j]]=="L" and i>=z):
				# print(i,k-a[j])
				flag=True
				break
		if(flag==True):
			# print(i,"lllllllllll")
			res[i]="W"
# print(res)
if(res[k]=="W"):
	print("First")
else:
	print("Second")


