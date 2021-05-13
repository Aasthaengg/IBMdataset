x=int(input())
ans=0
for i in range(1,x+1):
	if i%3!=0 and i%5!=0:
		ans=ans+i
print(ans)	