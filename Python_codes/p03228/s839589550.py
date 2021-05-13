a,b,k=map(int,input().split())
for i in range(k//2):
	if a%2:
		a=a-1
	a=a//2
	b=b+a
	if b%2:
		b=b-1
	b=b//2
	a=a+b

if k%2:
		if a%2:
			a=a-1
		a=a//2
		b=b+a
print('{} {}'.format(a,b))