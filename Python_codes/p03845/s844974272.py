def i():
	return int(input())
def i2():
	return map(int,input().split())
def s():
	return str(input())
def l():
	return list(input())
def intl():
	return list(int(k) for k in input().split())

n = i()
t = intl()
m = i()
p = []
x = []
for i in range(m):
	P,X = i2()
	p.append(P)
	x.append(X)

a = sum(t)
b = a
for i in range(m):
	a -= t[ p[i]-1 ] 
	a += x[i]
	print(a)
	a = b