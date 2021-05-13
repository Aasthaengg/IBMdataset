x=input()
x=list(x)
y='CODEFESTIVAL2016'
y=list(y)
z=len(x)
ans=0
for i in range(z):
	if x[i]!=y[i]:
		ans=ans+1
print(ans)