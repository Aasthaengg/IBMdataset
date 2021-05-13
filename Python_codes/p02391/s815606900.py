l = input().split()
l = list(map(int,l))
a,b = l[0],l[1]

if a>b:
	print('a > b')
elif a<b:
	print('a < b')
else:
	print('a == b')
