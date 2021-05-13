a=[0]*4
for i in range(3):
	x,y=map(int,input().split())
	a[x-1]+=1
	a[y-1]+=1
c=0
for i in range(4):
	if a[i]%2!=0:
		c+=1
if c==0 or c==2:
	print("YES")
else:
	print("NO")