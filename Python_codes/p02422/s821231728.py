s=list(input())
n=int(input())
for i in range(n):
	l=input().split()
	if l[0]=="replace":
		a=int(l[1])
		b=int(l[2])
		s[a:b+1]=list(l[3])
	elif l[0]=="reverse":
		a=int(l[1])
		b=int(l[2])
		c=s[a:b+1][::-1]
		s[a:b+1]=c
	else:
		a=int(l[1])
		b=int(l[2])
		print("".join(s[a:b+1]))