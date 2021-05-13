n=int(input())
a=2
b=1
a1=2
a2=1
for i in range(n-1):
	a=a1+a2
	a1=a
	a2=b
	b=a
if n==1:
	a=1
print(a)