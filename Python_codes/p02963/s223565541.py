n = int(input())
z = 1000000000
 
if n==z*z:
	print(z, 0, 0, z, 0, 0)
elif n > z:
    a = n//z
    b = n%z
    print(a+1, b, 0, z, 1, 0)
else:
    print(n, 0, 1, 1, 0, 0)