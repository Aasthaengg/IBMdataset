n,m  = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
P = 10**9+7

def s(n,i):
	return i * (n-(i-1))

def xx(x,n):
	t = 0
	for i in range(n-1):
		t = (t + s(n-1,i+1) * (x[i+1]-x[i])) % P
	return t

R = (xx(x,n) * xx(y,m)) % P 
print(R)
