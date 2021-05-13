def tri(a,b,c):
	return a**2 == b**2 + c**2
for time in range(int(input())):
	x,y,z = [int(i) for i in input().split()]
	if tri(x,y,z) or tri(y,z,x) or tri(z,x,y):
		print("YES")
	else:
		print("NO")