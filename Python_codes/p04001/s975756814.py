s=input()
ans=0
for i in range(2**(len(s)-1)):
	a=int(s[0])
	b=0
	for j in range(len(s)-1):
		if i&(1<<j)==0 :
			a=a*10+int(s[j+1])
		else:
			b+=a
			a=int(s[j+1])
	ans+=a+b
print(ans)