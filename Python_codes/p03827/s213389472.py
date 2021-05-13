n=int(input())
s=list(input())
a=0
b=0
for i in range(n):
	if s[i]=='I':
		a+=1
		if a>b:
			b=a
	else:
		a-=1
print(b)