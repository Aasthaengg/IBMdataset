def gcd(a,b):
	return a if b==0 else gcd(b,a%b)
def lcm(a,b):
	return a*b//gcd(a,b)
def f(n,c,d):
	return n-n//c-n//d+n//lcm(c,d)
A, B, C, D = map(int,input().split())
print(f(B,C,D)-f(A-1,C,D))