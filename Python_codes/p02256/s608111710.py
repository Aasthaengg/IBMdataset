def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

s=input().split()
a=int(s[0])
b=int(s[1])

y = gcd(a,b)
print(y)