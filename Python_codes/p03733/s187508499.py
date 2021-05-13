a,b=list(map(int, input().split()))
c=list(map(int, input().split()))

x=0
y=0
z=0
ans=0
for i in range(a-1):
	x=c[i]
	if c[i]<=c[i+1]-b:
		ans=ans+b
	else:
		ans=ans+c[i+1]-c[i]
print(ans+b)