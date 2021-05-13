n=int(input())
a=[int(x) for x in input().split()]
c=0 
for i in range(len(a)):
	if (i+1) & 1 and (a[i]&1):
		c+=1 	
print(c)