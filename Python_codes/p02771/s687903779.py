v = input().split()

v.sort()

if(v[0]==v[1] and v[0]!=v[2] or v[1]==v[2] and v[0]!=v[2]):
	print('Yes')
else:
	print('No')

	

