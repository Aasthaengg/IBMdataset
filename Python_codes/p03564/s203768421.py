A=int(input())
B=int(input())
z=1
for i in range(A):
	if z+B<2*z:
		z=z+B
	else:
		z=2*z
print(z)