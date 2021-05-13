def gcd(a,b):
	a,b=max(a,b),min(a,b)
	return a if b==0 else gcd(b,a%b)
def lcm(a,b):
	g=gcd(a,b)
	return a*b//g
n=int(input())
t=[int(input()) for _ in range(n)]
t=list(set(t))
l=t[0]
for i in t[1:]:
	l=lcm(l,i)
print(l)