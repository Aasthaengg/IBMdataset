a,b=map(int,input().split())
arr=list(map(int,input().split()))
c=1
s=0
for i in range(a):
	s+=arr[i]
	if s<=b:
		c+=1
	else:
		break	
		
print(c)		