n=int(input())
a=[int(i) for i in input().split()]
b=sorted(a)
x=sum(b[-1:])
y=sum(b[:-1])
if y>x:
	print('Yes')
else:
	print('No')