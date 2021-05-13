k,s = map(int, input().split())
c=0
for i in range(k+1):
	for j in range(k+1):
		if s>=i+j and k+1+i+j>s :
			c+=1
			# print( c )

print( c )