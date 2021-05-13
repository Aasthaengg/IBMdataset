s=input()
t=input()
a=0
f=False

for i in range(len(s)):
	a=s[-1]
	s=s[:-1]
	s=a+s
	
	if s==t:
		f=True
		break
		
if f:
	print('Yes')
else:
	print('No')