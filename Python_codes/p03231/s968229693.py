def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
def lcm(a, b):
	return a * b // gcd (a, b)
 
n,m = map(int,input().split())
s = input()
t = input()

l = lcm(n,m)
gaps = l//m
gapt = l//n

i,j = 0,0
while i<n:
    if s[i]!=t[j]:
        print(-1)
        break
    else:
        i += gaps
        j += gapt
else:
    print(l)