n=int(input())
s=input()
t=input()
p=0
i=0
ans=1
while i<n:
	if s[i]==t[i]:
		if p==0:
			ans*=3
		elif p=="x":
			ans*=2
		p="x"
		ans%=(10**9+7)
		i+=1
	else:
		if p==0:
			ans*=6
		elif p=="x":
			ans*=2
		else:
			ans*=3
		p="y"
		ans%=(10**9+7)
		i+=2
print(ans)

